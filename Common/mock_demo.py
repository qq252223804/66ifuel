from mock import mock
def mock_test(url,method,request_data,response_data):
    mock_method = mock.Mock(return_value=response_data)
    mock_res=mock_method(url,method,request_data)    #用模拟请求方式获得模拟数据
    return mock_res
