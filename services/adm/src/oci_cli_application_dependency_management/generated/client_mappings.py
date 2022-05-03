# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.adm import ApplicationDependencyManagementClient

MODULE_TO_TYPE_MAPPINGS["adm"] = oci.adm.models.adm_type_mapping
if CLIENT_MAP.get("adm") is None:
    CLIENT_MAP["adm"] = {}
CLIENT_MAP["adm"]["application_dependency_management"] = ApplicationDependencyManagementClient
