# Cat-Facts
Get random cat (and dog) facts

[https://mcm-tt21-cat-facts.herokuapp.com/](https://mcm-tt21-cat-facts.herokuapp.com/)

### Get facts

Retrieve one or more `Facts`.

##### Endpoint
`GET /api/v1/facts`

##### Query parameters

| Parameter   | Type                   | Default | Limit | Description                                                                                                                                           |
| ----------- | ---------------------- | ------- | ----- | -----------------------------------------
| animal_type | Comma-separated String | 'cat'   |       | Type of animal the fact will describe                                                                                       |
| id          | Number                 |         | 500   | (optional) ID of a specific fact to return, will return a random fact if left blank  

##### Example request
`GET /facts/?animal_type=cat`

```json
{
	"id":111,
	"text":"A cat can travel at a top speed of approximately 31 mph (49 km) over a short distance"
}
```
