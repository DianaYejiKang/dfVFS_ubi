#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the RAW image resolver helper implementation."""

import unittest

from dfvfs.lib import definitions
from dfvfs.path import factory as path_spec_factory
from dfvfs.resolver_helpers import raw_resolver_helper

from tests.resolver_helpers import test_lib


class RawResolverHelperTest(test_lib.ResolverHelperTestCase):
  """Tests for the RAW image resolver helper implementation."""

  def setUp(self):
    """Sets up the needed objects used throughout the test."""
    super(RawResolverHelperTest, self).setUp()

    test_path = self._GetTestFilePath(['ext2.raw'])
    self._SkipIfPathNotExists(test_path)

    test_os_path_spec = path_spec_factory.Factory.NewPathSpec(
        definitions.TYPE_INDICATOR_OS, location=test_path)
    self._raw_path_spec = path_spec_factory.Factory.NewPathSpec(
        definitions.TYPE_INDICATOR_RAW, parent=test_os_path_spec)

  def testNewFileObject(self):
    """Tests the NewFileObject function."""
    resolver_helper_object = raw_resolver_helper.RawResolverHelper()
    self._TestNewFileObject(resolver_helper_object, self._raw_path_spec)

  def testNewFileSystem(self):
    """Tests the NewFileSystem function."""
    resolver_helper_object = raw_resolver_helper.RawResolverHelper()
    self._TestNewFileSystemRaisesNotSupported(
        resolver_helper_object, self._raw_path_spec)


if __name__ == '__main__':
  unittest.main()
