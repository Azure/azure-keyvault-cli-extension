import os, sys, argparse, shutil
from subprocess import Popen, PIPE
from distutils.dir_util import copy_tree, remove_tree

_source_md = '### Source Origin:'
_replacements = {
    'azure.keyvault': 'azext_keyvault.keyvault',
    'azure.mgmt.keyvault': 'azext_keyvault.mgmt.keyvault',
    'azure.cli.command_modules.keyvault': 'azext_keyvault'
}

def run_process(cmd, cwd):
    p = Popen(cmd, stdout=PIPE, stderr=PIPE, cwd=cwd)
    stdout, stderr = p.communicate()
    p.wait()
    if stderr:
        print('ERROR: %s' % stderr)
    return stdout.decode('utf-8').strip() if not stderr else None


def list_repo_files(dir):
    ls_tree_out = run_process('git ls-tree -r --name-only HEAD', cwd=dir)

    return [os.path.join(dir, file) for file in ls_tree_out.split()]


def copy_file(src, dst, replacements=None):

    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    _, extension = os.path.splitext(src)
    if extension.lower() == '.py':
        with open(src, mode='r') as s:
            with open(dst, mode='w') as d:
                # if replacements are specified replace line by line
                if replacements:
                    old = s.readline()
                    while(old):
                        new = old
                        for orig, repl in replacements.items():
                            new = new.replace(orig, repl)

                        if len(old) != len(new):
                            print('\n\t-%s\t+%s' % (old, new))

                        d.write(new)
                        old = s.readline()

                # if no replacements are specified write the remainder of the file
                else:
                    d.write(s.read())
    else:
        shutil.copyfile(src, dst)


def copy_repo_files(src, dst, repo_name, replacements=None):

    branch = run_process('git rev-parse --abbrev-ref HEAD', cwd=src)
    head = run_process('git rev-parse HEAD', cwd=src)

    if not (branch and head):
        print('unable to obtain branch info from "%s"' % src)
        exit(1)

    tag = '%s/%s %s' % (repo_name, branch, head)

    print('copying %s:\n\t %s' % (src, tag))

    for src_file in list_repo_files(src):
        dst_file = src_file.replace(src, dst)
        print(dst_file)

        copy_file(src_file, dst_file, replacements)

    return tag


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--sdk', help='the root directory of the local azure-sdk-for-python clone', required=True)
    parser.add_argument('--cli', help='the root directory of the local azure-cli clone', required=True)
    args = parser.parse_args()

    sdk_root = args.sdk
    cli_root = args.cli
    repo_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
    ext_root = os.path.join(repo_root, 'azext_keyvault')

    data_sdk_src = os.path.join(sdk_root, 'azure-keyvault/azure/keyvault')
    mgmt_sdk_src = os.path.join(sdk_root, 'azure-mgmt-keyvault/azure/mgmt')

    data_sdk_dst = os.path.join(ext_root, 'keyvault')
    mgmt_sdk_dst = os.path.join(ext_root, 'mgmt')

    cli_src = os.path.join(cli_root, 'src/command_modules/azure-cli-keyvault/azure/cli/command_modules/keyvault')

    # delete exiting extension files
    if os.path.exists(ext_root):
        remove_tree(ext_root)

    # copy sdk files
    sdk_tag = copy_repo_files(mgmt_sdk_src, mgmt_sdk_dst, 'azure-sdk-for-python')
    sdk_tag = copy_repo_files(data_sdk_src, data_sdk_dst, 'azure-sdk-for-python')

    # copy cli files
    cli_tag = copy_repo_files(cli_src, ext_root, 'azure-cli', _replacements)

    # write the sources.md file
    with open(os.path.join(ext_root, 'source.md'), 'w') as f:
        f.write('\n\t'.join([_source_md, sdk_tag, cli_tag]) + '\n')

    # copy the azext_metadata.json
    md_src = os.path.join(repo_root, 'azext_metadata.json')
    md_dst = os.path.join(ext_root, 'azext_metadata.json')
    copy_file(md_src, md_dst, None)
