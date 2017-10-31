#!/usr/bin/env python

import click
import os
import sys
from StringIO import StringIO

@click.command()
@click.option('--provider',
              default='rhev',
              type=click.Choice(['rhev']),
              help='This option specifies provider platform. ',
              show_default=True)
@click.option('--deploy_type',
              default='ocp',
              type=click.Choice(['ocp', 'scale', 'bg_upgrade', 'logging', 'metrics', 'ansible-controller']),
              help='This option specifies main commands : deploying a new cluster, scaling up/down nodes, blue green upgrade',
              show_default=True)
@click.option('--operate',
              type=click.Choice(['deploy', 'undeploy', 'start', 'stop', 'teardown', 'up', 'down', 'warmup', 'upgrade']),
              help='This option specifies sub commands : deploying a new cluster, start/stop/teardown VMs, scaling up/down')
@click.option('--tag',
              help='The tag of cluster used for targeting specific cluster operated to. It will overwrite the value from vars/all ')
@click.option('--target_node_filter',
              help='The filter for VMs in the cluster tag')
@click.option('--ocp_version',
              help='openshift verion. Basically, it will come from vars/all file but it can be overwritten ')
@click.option('--ocp_install',
              is_flag=False,
              help='Adding this flag will delete VM without cordon/drain tasks. This flag is useful for teardown of cluster')
@click.option('--target',
              type=click.Choice(['app', 'infra', 'master', 'node']),
              help='Target node: app/infra for scale, master/node for bg upgrade')
@click.option('--force',
              default=False,
              help='Ignore validation and force to rewrite configuration event though it exists')
@click.option('--new_cluster_color',
              type=click.Choice(['green', 'blue', None]),
              default=None,
              help='When error happen during bg upgrade, color can be overwritten not to create new nodes.')
@click.option('--instances',
              default='1',
              help='Specifying how many vms will be scaling up/down')
@click.help_option('--help', '-h')
@click.option('-v', '--verbose', count=True)
def launch(provider=None,
           deploy_type=None,
           operate=None,
           tag=None,
           target_node_filter=None,
           ocp_version=None,
           target=None,
           instances=None,
           ocp_install=None,
           force=None,
           new_cluster_color=None,
           verbose=0):

    # validate ocp deploy_type options
    if deploy_type == 'ocp':
        if target is not None:
            print "--target option is for scale/bg_upgrade"
            sys.exit(1)

        if operate not in ['deploy', 'start', 'stop', 'teardown']:
            print "operate (deploy/start/stop/teardown) only allowed for ocp"
            sys.exit(1)

    # validate scale deploy_type options
    if deploy_type == 'scale':
        if target is None:
            print "--target_node_filter option is for ocp"
            sys.exit(1)

        if operate not in ['up', 'down']:
            print "operate (up/down) only allowed for scale deploy_type"
            sys.exit(1)

    # validate bg_upgrade deploy_type options
    if deploy_type == 'bg_upgrade':
        if target is None:
            print "target option is essential for bg_upgrade"
            sys.exit(1)

        if operate not in ['deploy', 'warmup']:
            print "operate (deploy/warmup) only allowed for bg_upgrade deploy_type"
            sys.exit(1)

    # validate bg_upgrade deploy_type options
    if deploy_type == 'ansible_controller':
        if target_node_filter is not None:
            print "--target_node_filter option is for ocp"
            sys.exit(1)

        if instances is not None:
            print "--instances option is for scale"
            sys.exit(1)

        if operate is not None:
            print "operate is not allowed"
            sys.exit(1)

        if target is not None:
            print "--target option is for scale/bg_upgrade"
            sys.exit(1)


    if verbose > 0:
        verbosity = '-' + 'v' * verbose
    else:
        verbosity = ''



    # Create variable list to overwrite
    all_variables_str= ["provider", "deploy_type", "operate", "tag", "target_node_filter", "ocp_install", "target", "instances", "ocp_version", "force_rewrite", "new_cluster_color"];
    all_variables_real= [provider, deploy_type, operate, tag, target_node_filter, ocp_install, target, instances, ocp_version, force, new_cluster_color];
    overwrite_variables=[];
    var_index=0
    sio=StringIO();
    for variable in all_variables_real:
        if variable is not None:
            real_value=str(variable);
            add_value=all_variables_str[var_index]+"="+real_value;
            overwrite_variables.append(add_value);
          #  overwrite_variables.append(add_value);
          #  ''.join(overwrite_variables)
          #  print overwrite_variables;

        var_index += 1

    sio.write(' '.join(overwrite_variables));
    print sio.getvalue();




# Construct ansible command
    if deploy_type == 'ansible-controller':
        status = os.system(
             'ansible-playbook %s playbooks/%s/ansible-controller.yaml \
             --extra-vars "@vars/all" \
             --extra-vars "@vars/ocp_params" \
             -e "%s"'
             % (verbosity, provider, sio.getvalue())
        )
    else:
        status = os.system(
            'ansible-playbook %s playbooks/config.yaml \
            --extra-vars "@vars/all" \
            --extra-vars "@vars/ocp_params" -e retry_scale=false \
            -e "%s"'
            % (verbosity, sio.getvalue())
              
        )

    # Exit appropriately
    if os.WIFEXITED(status) and os.WEXITSTATUS(status) != 0:
        sys.exit(os.WEXITSTATUS(status))


if __name__ == '__main__':
    launch(auto_envvar_prefix='RHEV_OCP_DEPLOY')
