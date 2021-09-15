# Challenge 2
This script will fetch the AWS EC2 instance meta-data.
This has to be executed inside EC2 instance you do not need to use the Amazon EC2 console or the AWS CLI.  
Reference : https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html

## prerequisites
1. python3 should be installed
2. make sure to install _requests_ module if not present
    ```
    pip3 install requests
    ```

## How to Execute
```
python3 metadata.py
```
## Output

```python
$ python3 metadata.py
please enter data key to query:public-ipv4
{
    "public-ipv4": "1.2.3.4"
}
```

> **Note**: Currently only below values are allowed for data key
```
ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
events/
hostname
iam/
instance-action
instance-id
instance-life-cycle
instance-type
local-hostname
local-ipv4
mac
metrics/
network/
placement/
profile
public-hostname
public-ipv4
public-keys/
reservation-id
security-groups
services/
```