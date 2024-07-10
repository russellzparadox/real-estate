## api request Helper

the base of every API request is ``/api/``

## status List Api:

- endPoint : `/api/status`
- method : ``GET``
- response :

```json
[
  {
    "id": 1,
    "name": "stat1"
  },
  {
    "id": 2,
    "name": "stat2"
  }
]
```

## type of property use Lists API:

*همون نوع کاربری*

- endPoint : `/api/topu`
- method : ``GET``
- response :

```json
[
  {
    "id": 1,
    "name": "t1"
  },
  {
    "id": 2,
    "name": "t1"
  }
]
```

## province List API:

*list all provinces*

- endPoint : `/api/provinces`
- method : ``GET``
- response :

```json
[
  {
    "id": 1,
    "name": "آذربایجان شرقی",
    "amar_code": 3
  },
  {
    "id": 2,
    "name": "آذربایجان غربی",
    "amar_code": 4
  },
  {
    "id": 3,
    "name": "اردبیل",
    "amar_code": 24
  },
  "..."
]
```

## list cities that are from a province:

- endPint : `api/provinces/{int:province_id}/cities/`
- method : ``GET``
- response :

```json
[
  {
    "id": 31,
    "name": "آستانه",
    "amar_code": 7011112,
    "shahr_type": 0,
    "ostan": 28,
    "shahrestan": 269,
    "bakhsh": 985
  },
  {
    "id": 35,
    "name": "آشتیان",
    "amar_code": 2011103,
    "shahr_type": 0,
    "ostan": 28,
    "shahrestan": 11,
    "bakhsh": 978
  },
  {
    "id": 46,
    "name": "آوه",
    "amar_code": 6032827,
    "shahr_type": 0,
    "ostan": 28,
    "shahrestan": 236,
    "bakhsh": 984
  },
  {
    "id": 61,
    "name": "اراک",
    "amar_code": 1021101,
    "shahr_type": 0,
    "ostan": 28,
    "shahrestan": 19,
    "bakhsh": 977
  },
  "..."
]
```

## Create Case (*آگهی*)

- endPint : `api/cases`
- method : ``POST``
- request body:

```json
{
  "title": "Sample Case",
  "land": {
    "lat": 35.6895,
    "long": 139.6917,
    "address": "Tokyo, Japan",
    "province": provinceID,
    "city": CityID,
    "areaOfBuilding": 100.5,
    "areaOfLand": 200.5,
    "electricityAmper": 20.5,
    "edari": "Office",
    "buildingHeight": 30.5,
    "phoneNumber": "+815012345678",
    "secondaryPhoneNumber": "+815012345679",
    "ownerName": "John Doe",
    "image": null,
    "features": [
      {
        "name": "Feature1"
      },
      {
        "name": "Feature2"
      }
    ],
    "privetNote": "Some private note.",
    "status": StatusID,
    "typeOfPropertyUse": TOPU_ID
  },
  "content": "Case content goes here.",
  "sellPrice": 2000000,
  "rentPrice": 50000
}
```

- **required fields**:
  میگم حالا

# List Cases

- endPint : `api/cases`
- method : ``GEt``
- response:
```json
[
  {
    "id": 1,
    "title": "Sample Case",
    "land": {
      "lat": 35.6895,
      "long": 139.6917,
      "address": "Tokyo, Japan",
      "province": null,
      "city": null,
      "areaOfBuilding": 100.5,
      "areaOfLand": 200.5,
      "electricityAmper": 20.5,
      "edari": "Office",
      "buildingHeight": 30.5,
      "phoneNumber": "+815012345678",
      "secondaryPhoneNumber": "+815012345679",
      "ownerName": "John Doe",
      "image": null,
      "features": [
        {
          "id": 1,
          "name": "Feature1"
        },
        {
          "id": 2,
          "name": "Feature2"
        }
      ],
      "privetNote": "Some private note.",
      "status": null,
      "typeOfPropertyUse": null
    },
    "content": "Case content goes here.",
    "sellPrice": 1000000,
    "rentPrice": 50000
  },
  {
    "id": 2,
    "title": "Sample Case",
    "land": {
      "lat": 35.6895,
      "long": 139.6917,
      "address": "Tokyo, Japan",
      "province": null,
      "city": null,
      "areaOfBuilding": 100.5,
      "areaOfLand": 200.5,
      "electricityAmper": 20.5,
      "edari": "Office",
      "buildingHeight": 30.5,
      "phoneNumber": "+815012345678",
      "secondaryPhoneNumber": "+815012345679",
      "ownerName": "John Doe",
      "image": null,
      "features": [
        {
          "id": 1,
          "name": "Feature1"
        },
        {
          "id": 2,
          "name": "Feature2"
        }
      ],
      "privetNote": "Some private note.",
      "status": null,
      "typeOfPropertyUse": null
    },
    "content": "Case content goes here.",
    "sellPrice": 1000000,
    "rentPrice": 50000
  },
  "..."
]
```
    