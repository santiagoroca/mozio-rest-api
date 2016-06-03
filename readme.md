# Mozio RestAPI


## Enpoints Documentation


## /provider

Methods | Available
------------ | -------------
POST | :heavy_check_mark:
GET |
PUT | :heavy_check_mark:
DELETE | :heavy_check_mark:

## * POST

**Payload**

```
	[
		{
			"name": [string], //User's first and lastname.
			"email": [string], //User's email
			"phone_number": [string], //User's personal phone number
			"language": [string], //User's language configuration
			"currency": [string] //User's curency
		}
	]
```

**Example Payload**

```
	[
		{
			"name": "Foo Bar".
			"email": "foo@bar.com"
			"phone_number": "0303456"
			"language": "ES"
			"currency": "9999"
		}
	]
```

**Returns**

STATUS 
201: Newly inserted object || 
400: Error Message(s)

```
	{
		"name": [string], //User's first and lastname.
		"email": [string], //User's email
		"phone_number": [string], //User's personal phone number
		"language": [string], //User's language configuration
		"currency": [string] //User's curency
	}
```

## /provider/{id}

## * PUT

**Payload**

```
	[
		{
		"name": [string], //User's first and lastname.
		"email": [string], //User's email
		"phone_number": [string], //User's personal phone number
		"language": [string], //User's language configuration
		"currency": [string] //User's curency
		}
	]
```

**Example Payload**

```
	[
		{
		"name": "Bar Foo".
		"email": "bar@foo.com"
		"phone_number": "6543030"
		"language": "EN"
		"currency": "1111"
		}
	]
```

**Returns**

STATUS
200: Updated object || 
400: Error Message(s)

**Return Body**

```
	{
		"id": [numeric], //Unique identifier for provider
		"name": [string], //User's first and lastname.
		"email": [string], //User's email
		"phone_number": [string], //User's personal phone number
		"language": [string], //User's language configuration
		"currency": [string] //User's curency
	}
```

## * DELETE

Methods | Available
------------ | -------------
POST |
GET | :heavy_check_mark:
PUT |
DELETE |


**Returns**

STATUS
200: Empty || 
400: Error Message(s)


## * GET

**Options**

Parameter  | Description | Example
------------ |------------ | -------------
lat | When lat provided, provider list will reduce to all areas providers which area contains this position | /provider?lat=15.5 
lon | When lon provided, provider list will reduce to all areas providers which area contains this position | /provider?lat=17.5

**Returns**
STATUS
200: Providers List || 
400: Error Message(s)

**Return Body**

```
	[
		{
			"id": [numeric], //Unique identifier for provider
			"name": [string], //User's first and lastname.
			"email": [string], //User's email
			"phone_number": [string], //User's personal phone number
			"language": [string], //User's language configuration
			"currency": [string] //User's curency
		},
		...
	]
```



## /provider/{id}/polygon

## * GET

Methods | Available
------------ | -------------
POST |
GET | :heavy_check_mark:
PUT |
DELETE |

**Returns**

STATUS
200: Providers List

**Return Body**

```
	[
		{
			"id": [numeric], //unique indentifier for polygon
			"provider": [numeric], //owner provider id
			"name": [strnig] //Polygon area name
		},
		...
	]
```



## /polygon

Methods | Available
------------ | -------------
POST | :heavy_check_mark:
GET |
PUT |
DELETE |

## * POST

**Example Payload**
```
	[
		{
			"provider": [numeric], //Provider id to asociate to
			"name": [string] //area name
		}
	]
```

**Returns**

STATUS
201: Newly Polygon Created || 
400: Error Message(s)

**Return Body**
```
	{
		"id": [numeric], //unqiue identifier
		"provider": [numeric], //Provider id to asociate to
		    "name": [string] //area name,
	}
```



## /polygon/{id}/point

## * GET

Methods | Available
------------ | -------------
POST |
GET | :heavy_check_mark:
PUT |
DELETE |

**Returns**
STATUS
200: Point List

**Options**

Parameter  | Description | Example
------------ |------------ | -------------
geogson | when 'True' body will be returned in geojson format

**Return Body**

```
    [
        {
            "id": [numeric], //unique indentifier
            "polygon": [numeric], //ascoiated polygon id
            "lat": [numeric], //Latitude
            "lon": [numeric] //longitude
        },
      ...
    ]
```

**Return Body GeoJson Example**

```
	{
	"type": "Polygon",
		"coordinates": [
			[
			  14.5,
			  17.5
			],
			[
			  19.5,
			  18.6
			],
			[
			  25.5,
			  8.6
			]
		]
}
```


## /point

Methods | Available
------------ | -------------
POST | :heavy_check_mark:
GET |
PUT |
DELETE |

## * POST

**Example Payload**
```
[
{
    "polygon": [numeric], //ascoiated polygon id
    "lat": [numeric], //Latitude
    "lon": [numeric] //longitude
}
]
```

**Returns**
STATUS
201: Newly Point Created || 
400: Error Message(s)

**Return Body**
```
	{
	    "id": [numeric], //unique indentifier
	    "polygon": [numeric], //ascoiated polygon id
	    "lat": [numeric], //Latitude
	    "lon": [numeric] //longitude
	}
```

