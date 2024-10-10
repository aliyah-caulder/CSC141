# Imports module from describe_function and calls it using different import techniques.

import describe_function

describe_function.describe_city('Baltimore')

from describe_function import describe_city

describe_city('Baltimore')

from describe_function import describe_city as dc

dc('Baltimore')

import describe_function as df

df.describe_city('Baltimore')

from describe_function import *

describe_city('Baltimore')