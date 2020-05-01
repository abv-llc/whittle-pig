# Python Package Inclusion On Lambda

Dockerize, download and zip required packages and code as a lambda layer

#### Sources
[Creating New AWS Lambda Layer For Python Pandas Library](https://medium.com/@qtangs/creating-new-aws-lambda-layer-for-python-pandas-library-348b126e9f3e)
[How to use AWS Lambda Layers](https://medium.com/faun/how-to-use-aws-lambda-layers-f4fe6624aff1)

## Defining package requirements

The `requirements.txt` file contains `pandas` (and potentially other) libraries.
`pandas` depends on `numpy` as well, but since there is already a `Lambda Layer` for 
`numpy` provided by AWS, we should make use of that in our functions instead of 
including `numpy` in this custom `pandas` layer. That’s essentially one of the 
beauties of using `Lambda Layers`, code reuse.

## Defining the Lambda Handler

Test the lambda function locally, install required packages and
update the `requirements.txt` file accordingly. When ready, execute
the following commands:

```python
sh get_layer_packages.sh
sh zip_layer_packages.sh
```

## Adding the Lambda Layer

Add the new layer as an uploaded zip file in the Lambda portion of the AWS Console
