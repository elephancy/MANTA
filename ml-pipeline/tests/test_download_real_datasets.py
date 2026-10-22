from __future__ import annotations

import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.request import Request

from ml_pipeline import download_real_datasets as datasets


class DatasetDownloadTests(unittest.TestCase):
    def test_approved_hosts_and_https_only(self):
        for url in ("https://codeload.github.com/org/repo/archive", "https://zenodo.org/api/records/123"):
            self.assertEqual(datasets.checked_dataset_url(url), url)
        for url in ("file:///etc/passwd", "http://zenodo.org/file", "https://zenodo.org.evil.invalid/file",
                    "https://other.invalid/file", "https://user:password@zenodo.org/file",
                    "https://zenodo.org:8443/file", "https://zenodo.org/file#fragment"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                datasets.checked_dataset_url(url)
            with self.subTest(redirect=url), self.assertRaises(ValueError):
                datasets.DatasetRedirectHandler().redirect_request(
                    Request("https://zenodo.org/file"), None, 302, "Found", {}, url)

    def test_download_streams_an_approved_response(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "dataset.zip"
            with patch.object(datasets, "open_dataset", return_value=io.BytesIO(b"fixture")):
                datasets._download("https://zenodo.org/file", target)
            self.assertEqual(target.read_bytes(), b"fixture")

    def test_file_url_is_rejected_without_writing_target(self):
        with tempfile.TemporaryDirectory() as directory:
            source, target = Path(directory) / "source", Path(directory) / "target"
            source.write_text("local-only-fixture")
            with self.assertRaises(ValueError):
                datasets._download(source.as_uri(), target)
            self.assertFalse(target.exists())

    def test_zenodo_file_cannot_escape_output_directory(self):
        for filename in ("../escape", "nested/file", "nested\\file", "C:escape", ".", ".."):
            payload = {"files": [{"key": filename, "links": {"self": "https://zenodo.org/file"}}]}
            with tempfile.TemporaryDirectory() as directory:
                with patch.object(datasets, "open_dataset", return_value=io.BytesIO(json.dumps(payload).encode())):
                    with self.subTest(filename=filename), self.assertRaises(ValueError):
                        datasets.download_zenodo_record({"record_id": "123"}, Path(directory), "*")

    def test_record_identifier_is_numeric(self):
        with self.assertRaises(ValueError):
            datasets.download_zenodo_record({"record_id": "../../other"}, Path("."), "*")
