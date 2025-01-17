#   Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from common_import import *


@benchmark_registry.register("equal_all")
class EqualAllConfig(APIConfig):
    def __init__(self):
        super(EqualAllConfig, self).__init__("equal_all")
        self.run_tf = False


@benchmark_registry.register("equal_all")
class PaddleEqualAll(PaddleOpBenchmarkBase):
    def build_graph(self, config):
        x = self.variable(name='x', shape=config.x_shape, dtype=config.x_dtype)
        y = self.variable(name='y', shape=config.y_shape, dtype=config.y_dtype)
        result = paddle.equal_all(x=x, y=y)

        self.feed_list = [x, y]
        self.fetch_list = [result]


@benchmark_registry.register("equal_all")
class TorchEqualAll(PytorchOpBenchmarkBase):
    def build_graph(self, config):
        x = self.variable(name='x', shape=config.x_shape, dtype=config.x_dtype)
        y = self.variable(name='y', shape=config.y_shape, dtype=config.y_dtype)
        result = torch.equal(input=x, other=y)
        result = torch.tensor(result)

        self.feed_list = [x, y]
        self.fetch_list = [result]
