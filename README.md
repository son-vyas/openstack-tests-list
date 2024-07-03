# openstack-tests-list
==========================

Overview
--------

openstack-tests-list will generate a skiplist/allowlist to be executed by tempest.
Each component can manage their own skiplist/allowlist or can use default.

-  Free software: Apache license

Quickstart
==========

- edit skiplist/alllowlist
- add the required fields
- execute tox tests
- submit :)

Installation
------------

Installing from git and virtualenv::

    $ git clone git@github.com:openstack-k8s-operators/openstack-tests-list.git
    $ cd openstack-tests-list

Examples
--------

A simple example of the structure of the yaml file expected by
openstack-test-lists.

.. code-block:: yaml

    known_failures:
    - test: 'full.tempest.test'
        bz: 'https://bugzilla.redhat.com/1'
        deployment:
          - 'undercloud'
          - 'overcloud'
        jobs:
          - job1
          - job2
        reason: 'default reason'
        releases:
          - name: master

In the above example, the test *full.tempest.test* will be skipped/excluded by tempest.
It will be skipped in the master release, specifically
in jobs job1 and job2. It will not be skipped in any other job, no matter what
the release is.

Removing the list of jobs, means it will be skipped everywhere.
