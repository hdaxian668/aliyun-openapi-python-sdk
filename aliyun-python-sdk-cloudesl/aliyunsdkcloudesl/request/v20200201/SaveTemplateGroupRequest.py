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
from aliyunsdkcloudesl.endpoint import endpoint_data

class SaveTemplateGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudesl', '2020-02-01', 'SaveTemplateGroup')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TemplateVersion(self):
		return self.get_body_params().get('TemplateVersion')

	def set_TemplateVersion(self,TemplateVersion):
		self.add_body_params('TemplateVersion', TemplateVersion)

	def get_EslModelId(self):
		return self.get_body_params().get('EslModelId')

	def set_EslModelId(self,EslModelId):
		self.add_body_params('EslModelId', EslModelId)

	def get_GroupId(self):
		return self.get_body_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_body_params('GroupId', GroupId)

	def get_WidthPx(self):
		return self.get_body_params().get('WidthPx')

	def set_WidthPx(self,WidthPx):
		self.add_body_params('WidthPx', WidthPx)

	def get_GroupName(self):
		return self.get_body_params().get('GroupName')

	def set_GroupName(self,GroupName):
		self.add_body_params('GroupName', GroupName)

	def get_HeightPx(self):
		return self.get_body_params().get('HeightPx')

	def set_HeightPx(self,HeightPx):
		self.add_body_params('HeightPx', HeightPx)