import json

from com.huawei.iotplatform.client.invokeapi.Authentication import Authentication
from com.huawei.iotplatform.client.invokeapi.DataCollection import DataCollection

from com.huawei.iotplatform.client.dto.AuthOutDTO import AuthOutDTO
from com.huawei.iotplatform.client.dto.QueryBatchDevicesInfoInDTO import QueryBatchDevicesInfoInDTO
from com.huawei.iotplatform.client.dto.QueryDeviceCapabilitiesInDTO import QueryDeviceCapabilitiesInDTO
from com.huawei.iotplatform.client.dto.QueryDeviceDataHistoryInDTO import QueryDeviceDataHistoryInDTO
from com.huawei.iotplatform.client.dto.QueryDeviceDesiredHistoryInDTO import QueryDeviceDesiredHistoryInDTO
from com.huawei.iotplatform.constant.Constant import Constant


class DataCollectionTest(object):
    def queryBatchDevicesInfo(self):
        qbdiInDTO = QueryBatchDevicesInfoInDTO()
        qbdiInDTO.gatewayId = "d7d2c6f6-d747-4c8b-a0d6-2dcef9343a76"
        qbdiInDTO.appId = "A_93xVRJbrZRrl5fjqP5W6CTxnMa"
        return qbdiInDTO

    def queryDeviceDataHistory(self):
        qddhInDTO = QueryDeviceDataHistoryInDTO()
        qddhInDTO.deviceId = "d7d2c6f6-d747-4c8b-a0d6-2dcef9343a76"
        qddhInDTO.gatewayId = "d7d2c6f6-d747-4c8b-a0d6-2dcef9343a76"
        qddhInDTO.appId = "A_93xVRJbrZRrl5fjqP5W6CTxnMa"
        qddhInDTO.pageSize = 100
        return qddhInDTO

    def queryDeviceDesiredHistory(self):
        qddhInDTO = QueryDeviceDesiredHistoryInDTO()
        qddhInDTO.deviceId = "d7d2c6f6-d747-4c8b-a0d6-2dcef9343a76"
        qddhInDTO.gatewayId = "d7d2c6f6-d747-4c8b-a0d6-2dcef9343a76"
        qddhInDTO.appId = "A_93xVRJbrZRrl5fjqP5W6CTxnMa"
        return qddhInDTO

    def queryDeviceCapabilities(self):
        qdcInDTO = QueryDeviceCapabilitiesInDTO()
        qdcInDTO.deviceId = "d7d2c6f6-d747-4c8b-a0d6-2dcef9343a76"
        qdcInDTO.gatewayId = "d7d2c6f6-d747-4c8b-a0d6-2dcef9343a76"
        qdcInDTO.appId = "A_93xVRJbrZRrl5fjqP5W6CTxnMa"
        return qdcInDTO


if __name__ == "__main__":
    dcTest = DataCollectionTest()
    authentication = Authentication()
    dataCollection = DataCollection()

    # get accessToken at first
    result = authentication.getAuthToken(Constant().clientInfo())
    authOutDTO = AuthOutDTO()
    authOutDTO.setAccessToken(json.loads(result)['accessToken'])
    accessToken = authOutDTO.getAccessToken()

    # query device info
    deviceId = "d7d2c6f6-d747-4c8b-a0d6-2dcef9343a76"
    dq = dataCollection.querySingleDeviceInfo(deviceId, None, None, accessToken)
    print("====== query device info ======")
    print("result:", dq + "\n")

    # # query batch device info
    # dataCollection.queryBatchDevicesInfo(dcTest.queryBatchDevicesInfo(), accessToken)
    # print("====== query batch device info ======")
    # print("result:", dq + "\n")

    # query device data history
    dq = dataCollection.queryDeviceDataHistory(dcTest.queryDeviceDataHistory(), accessToken)
    print("====== query device data history ======")
    print("result:", dq + "\n")

    # # query device desired history
    # dq = dataCollection.queryDeviceDesiredHistory(dcTest.queryDeviceDesiredHistory(), accessToken)
    # print("====== query device desired history ======")
    # print("result:", dq + "\n")
    #
    # # query device desired capabilities
    # dq = dataCollection.queryDeviceCapabilities(dcTest.queryDeviceCapabilities(), accessToken)
    # print("====== query device desired capabilities ======")
    # print("result:", dq + "\n")
