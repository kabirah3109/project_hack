import argparse
import datetime
import json
import random
from big_entry import fill_random_value
import requests
import time
import form


def generate_request_body(url: str, only_required=False, idx=None, village=None):
    """Generate random request body data"""
    data = form.get_form_submit_request(
        url,
        only_required=only_required,
        fill_algorithm=fill_random_value,
        output="return",
        with_comment=False,
        idx=idx,
        village=village,
    )
    data = json.loads(data)
    return data


def submit(url: str, data: any):
    """Submit form to url with data"""
    url = form.get_form_response_url(url)
    # print("Submitting to", url)
    print("Data:", json.dumps(data), flush=True)

    res = requests.post(url, data=data, timeout=5)
    if res.status_code != 200:
        print(
            f"Error! Can't submit form {str(res.status_code)}: {res.reason}",
        )


def main(url, only_required=False, wards="Ogbomoso"):
    try:
        for i in range(0, 120):
            payload = generate_request_body(
                url, only_required=only_required, idx=i+1, village=wards
            )
            submit(
                url,
                payload,
            )
    except Exception as e:
        print("Error!", e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Submit google form with custom data")
    parser.add_argument("url", help="Google Form URL")
    parser.add_argument(
        "--ward",
        dest="ward",
        type=str,
        default="Ajaawa",
        help="Specify ward/location data",
    )
    parser.add_argument(
        "-r", "--required", action="store_true", help="Only include required fields"
    )
    args = parser.parse_args()
    main(url=args.url, only_required=args.required, wards=args.ward)
