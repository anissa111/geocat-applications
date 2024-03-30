import argparse
import json
import subprocess
import sys


def prev_curr(context):
    # get prev and curr commit if event type is push
    if context['event_name'] == 'push':
        return context['event']['before'], context['event']['after']

    # get prev and curr commit if event type is pull_request
    elif context['event_name'] == 'pull_request':
        print(f"{context['event']['pull_request']['base']['sha']} {context['event']['pull_request']['head']['sha']}")
        return context['event']['pull_request']['base']['sha'], context['event']['pull_request']['head']['sha']
    else:
        raise ValueError('Event type not supported')


def get_diff(context):
    base, head = prev_curr(context)

    # run git git_diff
    diff = subprocess.run(['git', 'git_diff', base, head, '--name-status'], capture_output=True, text=True).stdout
    diff = [e.split('\t') for e in diff.split('\n') if len(e) > 0]

    return diff


def get_new_modified(diff):
    new_and_modified = [e[1] for e in diff if e[0] in ['A', 'M']]

    return new_and_modified


def get_new_modified_notebooks(diff):
    new_and_modified_nb = [e[1] for e in diff if e[0] in ['A', 'M'] and e[1].endswith('.ipynb')]

    return new_and_modified_nb


def get_moved_deleted(diff):
    moved_and_deleted = [e[1] for e in diff if e[0] in ['D', 'R']]

    return moved_and_deleted


def get_changed_env_files(diff):
    changed_env = [e[1] for e in diff if
                   (e[1].endswith('.yml') or e[1].endswith('.yaml')) and not e[1].startswith('.github/workflows')]
    return changed_env


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('context_file', help='The JSON file containing the GitHub context')
    parser.add_argument('--env', action='store_true', help='Indicate only whether there are environment changes')
    parser.add_argument('--env-files', action='store_true', help='Return environment files that have been changed')
    parser.add_argument('--moved_deleted', action='store_true', help='Return files that have been moved or deleted')
    args = parser.parse_args()

    with open(sys.argv[1]) as f:
        github_context = json.load(f)

    git_diff = get_diff(github_context)
    out = get_new_modified(git_diff)

    if args.env:
        print('true' if len(get_changed_env_files(git_diff)) > 0 else 'false')
    elif args.env_files:
        print(get_changed_env_files(git_diff))
    elif args.moved_deleted:
        print(get_moved_deleted(git_diff))
    else:
        print(','.join(out) if len(out) > 0 else '')

