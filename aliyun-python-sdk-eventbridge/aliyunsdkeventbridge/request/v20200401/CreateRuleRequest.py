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
import json

class CreateRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'CreateRule')
		self.set_method('POST')

	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_RuleName(self): # String
		return self.get_query_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_query_param('RuleName', RuleName)
	def get_EventBusName(self): # String
		return self.get_query_params().get('EventBusName')

	def set_EventBusName(self, EventBusName):  # String
		self.add_query_param('EventBusName', EventBusName)
	def get_EventTargets(self): # Array
		return self.get_query_params().get('EventTargets')

	def set_EventTargets(self, EventTargets):  # Array
		self.add_query_param("EventTargets", json.dumps(EventTargets))
	def get_FilterPattern(self): # String
		return self.get_query_params().get('FilterPattern')

	def set_FilterPattern(self, FilterPattern):  # String
		self.add_query_param('FilterPattern', FilterPattern)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
