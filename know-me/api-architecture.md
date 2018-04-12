[Index](index.md)

---
## Api Architecture.

> Version the APIs

Allwas start the APR URI with somthing like this `/api/v{n}`
where n could be a number
or it could be the client type - version combination. `v-mobile-001`

> Array of Key-Value pair vs Array of Primitive types.

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

So we should as ourselved before creating an array of primitive data types.

> Is this array element part of an object with multiple attribute-properties? If so, never return an array of the object property. Instead prefer to send the array of attribute-property pair.
