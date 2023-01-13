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
from aliyunsdkcbn.endpoint import endpoint_data

class UpdateTransitRouterPeerAttachmentAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cbn', '2017-09-12', 'UpdateTransitRouterPeerAttachmentAttribute')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_BandwidthType(self): # String
		return self.get_query_params().get('BandwidthType')

	def set_BandwidthType(self, BandwidthType):  # String
		self.add_query_param('BandwidthType', BandwidthType)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_TransitRouterAttachmentName(self): # String
		return self.get_query_params().get('TransitRouterAttachmentName')

	def set_TransitRouterAttachmentName(self, TransitRouterAttachmentName):  # String
		self.add_query_param('TransitRouterAttachmentName', TransitRouterAttachmentName)
	def get_AutoPublishRouteEnabled(self): # Boolean
		return self.get_query_params().get('AutoPublishRouteEnabled')

	def set_AutoPublishRouteEnabled(self, AutoPublishRouteEnabled):  # Boolean
		self.add_query_param('AutoPublishRouteEnabled', AutoPublishRouteEnabled)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_Bandwidth(self): # Integer
		return self.get_query_params().get('Bandwidth')

	def set_Bandwidth(self, Bandwidth):  # Integer
		self.add_query_param('Bandwidth', Bandwidth)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_TransitRouterAttachmentId(self): # String
		return self.get_query_params().get('TransitRouterAttachmentId')

	def set_TransitRouterAttachmentId(self, TransitRouterAttachmentId):  # String
		self.add_query_param('TransitRouterAttachmentId', TransitRouterAttachmentId)
	def get_TransitRouterAttachmentDescription(self): # String
		return self.get_query_params().get('TransitRouterAttachmentDescription')

	def set_TransitRouterAttachmentDescription(self, TransitRouterAttachmentDescription):  # String
		self.add_query_param('TransitRouterAttachmentDescription', TransitRouterAttachmentDescription)
	def get_CenBandwidthPackageId(self): # String
		return self.get_query_params().get('CenBandwidthPackageId')

	def set_CenBandwidthPackageId(self, CenBandwidthPackageId):  # String
		self.add_query_param('CenBandwidthPackageId', CenBandwidthPackageId)
