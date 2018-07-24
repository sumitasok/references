[Index](index.md)

---
## Api Architecture.

####Version the APIs

Allways start the API URI with somthing like this `/api/v{n}`
where n could be a number
or it could be the client type - version combination. `v-mobile-001`

- Array of Key-Value pair vs Array of Primitive types.

The data structre of a Json is Arrays and Hashs. Its a Hash/Array, it can have nested hashes and arrays, and the arrays can in tern have Hashes.

The major reasons for Api version changes observed is, when the data was defines as an Array of primitive types. Now the expectation is to get Array of hashes.

For examples. An APi response is expected to have a list of companies.
Each company should have a list of managers names. So ew define the response as below.

/Api/v1/companies

```
{
	companies: [
		{
			company_id: 1234,
			name: 'Corp',
			managers: ['Sathya', 'sundar']
		}
	]
}
```

But when one of the consumer of the api demands the employee id of the managers to be send along the response. We are forced to chnage the whole structure of the API to

/api/v2/companies

```
{
	companies: [
		{
			company_id: 1234,
			name: 'Corp',
			managers: [
				{
					name: 'Sathya',
					employee_id: 'sathya001'
				},
				{
					 name: 'sundar',
					 employee_id: 'sundar002'
				 }
			 ]
		}
	]
}
```

Changing the api version `/api/v{n}` allows us to support clients that expect the name array as well as the client who wanted the employee id as well.

But this kind of api update request doent qualify for an api version change.

-  More over, the increase of versions for these small changes make it difficult to maintain the api's

But if we had implemented the managers array initialy itself as array of hash of manager, with only one key `name` we wouldnt have required this version change. Older clients would have ignored the new `employee_id` key and user the `name` key alone.

Never create an array of primitive data types.

> Is this array element part of an object with multiple attribute-properties? If so, never return an array of the object property. Instead prefer to send the array of attribute-property pair.


- using a standardised JSON request/response structure:

```
{
	"data" : {},
	"actions" : ["create", "invite"]
	"status": "",
	"message": ""
}
```

####Never create a dynamic key

Suppose we have to send the number of occurance of city in a data set,
Don't create a JSON in below format.

```
{
	"data" : {
		"Mumbai" : 2,
		"Bangalore" : 7
	}
}
```

The issue with this appraoch is, suppose any additional detail has to be send regarding the city, which is the object in question right now, we will have to change the structure of the API.

- Instead choose to make each city details part of an object, and the data an array of city objects.

```
{
	"data" : {
		"cities" : [
			{
				"name" : "Mumbai",
				"occurance" :  2
			},
			{
				"name" : "Bangalore",
				"occurance" : 7
			}
		]
	}
}
```

Taking care of these minute details while designing API from start, we can avoid

- a lot of API structure changes
- reaching out to API consumers with change requests.
- adding unnecssesary versions for the API.


With the above appraoch, we can add more key value pairs into the city object. __but never create a dynamic key__ unless the key itself is defined as value under another key.

Eg:

In a scenario, where I was sending status codes that the object passed through, along with data associated with those status code, I had taken a different approach.

a status code order-purchased require the API to have the time that transation happened and the mode of payment.
While in case of a state, order-cancelled, the API required to have the time of cancel, and who cancelled (Admin also can cancel the order)

At all time, an Order will have passed through multiple state, but will have only one current state.

- Some API will only require, the latest state details,
- while another might require detail of a particular state.
- and another will require all states and associated data for an order, with a reference to current state.


In below scenario, we are fetching details about `paid` state. So we need not send `cancelled` and `refunded` details. This below representation is to show the over all structure of the data. The amount of data in `details` key can be customised. Still a single Json parser will be able to handle both a single state query as well as a collection of states.

```
{
	"data" : {
		"order" : {
			"id" : 1000002,
			"states" : {
				"current" : "refunded",
				"detail-requested" : "paid",
				"details" : {
					"paid" : {
						"at" : "2018-07-02",
						"gateway" : "PayPal",
						"transition-sequence" : 0
					},
					"cancelled" : {
						"at" : "2018-07-03",
						"by" : {
							"name" : "Admin",
							"role" : "admin",
							"id" : "unique identifier"
						},
						"transition-sequence" : 1
					}
					"refunded" : {
						"at" : "2018-07-04",
						"gateway" : "PayPal",
						"transition-sequence" : 2
					}
				}
			}
		}
	}
}
```

The speciality of this scenario is, while we are using the state which is a data as a key as well, the states are always a finite set which can be considered as key.

Advantage of this approach is,

- For fetching a particular state data from the list is a Hash access O(1), instead of a loop on Array to find the expected state which has a O(n) complexity at client end.


Disadvantage is,

- The state transition order now has to be additionaly passed as a key value in the state data to indentify the state transition flow. So sorting the states would be a sort operation.
