# Type stubs for the Google Ads API Client Library for Python

[![PyPI version](https://badge.fury.io/py/google-ads-stubs.svg)](https://badge.fury.io/py/google-ads-stubs)

This package provides type stubs for the [Google Ads API Client Library for Python](https://github.com/googleads/google-ads-python). 
It's currently compatible with v18.1.0 of this library. It allows you to type check usage of the library with e.g. [mypy](http://mypy-lang.org/) and will also improve autocomplete in many editors.

**This is in no way affiliated with Google.**

Most stubs were created automatically by [stubgen](https://mypy.readthedocs.io/en/stable/stubgen.html), the rest are handwritten or generated by self-made scripts.

If you find incorrect annotations, please create an issue. Contributions for fixes are also welcome.

## Installation

```
$ pip install google-ads-stubs
```

## Caveats

There are some caveats. The primary one is that type inference does _not_ work for the `get_type` and `get_service`
methods of `Client`. The workaround is to explicitly state the type. For `get_type` you can also instantiate
the object directly.

```python
# Replace this:
campaign_operation = client.get_type('CampaignOperation')
# With this:
from google.ads.googleads.v10 import CampaignOperation
campaign_operation: CampaignOperation = client.get_type('CampaignOperation')
# Or this:
from google.ads.googleads.v10 import CampaignOperation
campaign_operation = CampaignOperation()

# Replace this:
google_ads_service = client.get_service('GoogleAdsService')
# With this:
from google.ads.googleads.v10 import GoogleAdsServiceClient
google_ads_service: GoogleAdsServiceClient = client.get_service('GoogleAdsService')
```

While it is technically possible to type these methods using a combination of overloading and literal types,
this is not included in these stubs. The reason is that it requires about 10,000 overloads, which makes most typecheckers fairly slow.

Another big caveat since v8.0.0 of this package is that the attributes and constructor arguments of the protobuf messages are all typed as `Any` instead of their proper types. This is due to `google-ads-python` switching from raw protobuf message classes to `proto-plus` classes. Better types for these might be introduced in the future. `GoogleAdsClient.enums` is also typed as `Any`.


Note that if you're using Mypy you need to use the `--namespace-packages` option as `google` and `google.ads` are namespace packages.