# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkdomain.endpoint import endpoint_data

class SaveBatchTaskForReserveDropListDomainRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'SaveBatchTaskForReserveDropListDomain','domain')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Domainss(self): # RepeatList
		return self.get_query_params().get('Domains')

	def set_Domainss(self, Domains):  # RepeatList
		for depth1 in range(len(Domains)):
			if Domains[depth1].get('Dns2') is not None:
				self.add_query_param('Domains.' + str(depth1 + 1) + '.Dns2', Domains[depth1].get('Dns2'))
			if Domains[depth1].get('Dns1') is not None:
				self.add_query_param('Domains.' + str(depth1 + 1) + '.Dns1', Domains[depth1].get('Dns1'))
			if Domains[depth1].get('DomainName') is not None:
				self.add_query_param('Domains.' + str(depth1 + 1) + '.DomainName', Domains[depth1].get('DomainName'))
	def get_ContactTemplateId(self): # String
		return self.get_query_params().get('ContactTemplateId')

	def set_ContactTemplateId(self, ContactTemplateId):  # String
		self.add_query_param('ContactTemplateId', ContactTemplateId)
