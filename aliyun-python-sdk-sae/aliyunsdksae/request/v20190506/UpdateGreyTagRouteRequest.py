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

from aliyunsdkcore.request import RoaRequest
from aliyunsdksae.endpoint import endpoint_data

class UpdateGreyTagRouteRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'sae', '2019-05-06', 'UpdateGreyTagRoute','serverless')
		self.set_uri_pattern('/pop/v1/sam/tagroute/greyTagRoute')
		self.set_method('PUT')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_GreyTagRouteId(self): # Long
		return self.get_query_params().get('GreyTagRouteId')

	def set_GreyTagRouteId(self, GreyTagRouteId):  # Long
		self.add_query_param('GreyTagRouteId', GreyTagRouteId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_DubboRules(self): # String
		return self.get_query_params().get('DubboRules')

	def set_DubboRules(self, DubboRules):  # String
		self.add_query_param('DubboRules', DubboRules)
	def get_ScRules(self): # String
		return self.get_query_params().get('ScRules')

	def set_ScRules(self, ScRules):  # String
		self.add_query_param('ScRules', ScRules)
