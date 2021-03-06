#! /usr/bin/env python3

from pathlib import Path
import subprocess
import tempfile

with tempfile.TemporaryDirectory(suffix="_nqdc") as tmp_dir:
    subprocess.run(
        [
            "nqdc",
            "run",
            "--plot_pub_dates",
            "-q",
            "fMRI[Abstract] AND aphasia[Title] "
            "AND (2017[PubDate] : 2019[PubDate])",
            tmp_dir,
        ]
    )
    assert (
        Path(tmp_dir)
        .joinpath(
            "query-49e0abb9869a532a31d37ed788c76780",
            "subset_allArticles_examplePluginPubDatesPlot",
            "plot.png",
        )
        .is_file()
    ), "Plugin output not found!"

print("nqdc and plugin ran successfully")
