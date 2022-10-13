import oci

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file("~/.oci/config")


# Initialize service client with default config file
monitoring_client = oci.monitoring.MonitoringClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
list_metrics_response = monitoring_client.list_metrics(
    compartment_id="ocid1.compartment.oc1..aaaaaaaaodl6djtpaff2r65z6oz62g32yfxwbmuvij6fttxretdpjygr4xgq",
    list_metrics_details=oci.monitoring.models.ListMetricsDetails(
        name="blhablah",
        namespace="oci_computeagent",
        resource_group="EXAMPLE-resourceGroup-Value"
        #dimension_filters={
            #'EXAMPLE_KEY_TNTbo': 'EXAMPLE_VALUE_Prsdms87OHp3nslWXCUO'},
        #group_by=["EXAMPLE--Value"],
        #sort_by="NAME",
        #sort_order="ASC"),
    #opc_request_id="QQXBSBSBJ0T6FBL9XYFB",
    #page="EXAMPLE-page-Value",
    #limit=361,
    ))

# Get the data from response
#print("nikesh")
print(list_metrics_response.data)