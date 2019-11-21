# Copyright 2019 Marcos Del Sol Vives <marcos@orca.pet>
# SPDX-License-Identifier: WTFPL

from collections import namedtuple
from saph import Saph
from unittest import TestCase

Vector = namedtuple('Vector', ('parts', 'memory', 'iters', 'hash'))

TEST_VECTORS = [
	Vector(['just', 'a', 'test'], 4, 2, '8a6d4f4a170929f264dae967748bf9f8f63ac732093ed439c444b044730109ff'),
	Vector([b'salt', b'pass'], 16384, 8, 'e1530ba599f87e4e62560e908f3db833cbefa97dc6cf9100d55df57a3a9e29ad'),
	Vector(['pepper', 'username', 'password'], 16384, 8, '38e48e2b1d4418766568e6212e59abb961b876b2a1f7f269752ed84afe6637c0'),
	Vector(['qepper', 'username', 'password'], 16384, 8, 'bb4a74eb50bab2e4cd334d93ee85d84f9c91f454ef33a68a484408747f0f391a')
]

class HashTest(TestCase):
	def test(self):
		for vector in TEST_VECTORS:
			s = Saph(memory=vector.memory, iterations=vector.iters)
			assert s.hash(*vector.parts).hex() == vector.hash
