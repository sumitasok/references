[Index](index.md)

---

## What is your approach to developing a code that is maintainable in a long term?

- Encapsulations: For every action create a separate method. Do not define an action in a combination method. Instead have separate methods for each action, then collect them to act in group using pipeline methods. - Single responsibility principle + pipeline methods.
Eg: If you have to create and send a PDF. One method for creating PDF, another method for sending of PDF or even generic method sending any file with address and sender details as parameters. A method to collect these two methods to run in series, as a pipeline. That way we can use PDF generator for another use case as saving of PDF to storage. We can use the send email for sending other documents as well.

- Test Driven Development. Write Tests. Both Unit and Integration.

- Every internal element should be Mockable, Stubbable and Fakeable.

- Setup pre-commit.com hooks to ensure code adheres to standards
- Setup a CI server.

- Use patterns like Decorator, Delegator for organising code better.

- Wrappers for all third party libraries. So we can switch the library without impacting code base. Test cover the wrappers.

- Json: never send an array of string if we are intending to send an array of particular property from an array of Objects. Instead send it as array of object with just the property attribute pair for forward compatibility.
Eg:

```
[{“name” : “sumit”}, {“name” : “dulqar”}]
```

instead of

```
[“sumit”, “dulqar”]
```
Don’t send primitive data types as array content. In real world we deal with resources. And resources comprises of attributes and properties. So if you array is carrying even a single attribute of objects, just send them as array of key-value pair. With key as the attribute of the object and value the property.

- Callbacks are mess. Pipelines are better.
- set methods private at the start, and make them public as and when it is utilised. Preferably expose pipelines alone.

- Write validations at 3 levels. Front end, back end and database level. Most applications reduce the validations to backend level. Not bad. But the best way to ensure uniqueness validation is at database level. if database provide atomic operations use that. Some are lazy and l put validations at front end alone. That should be avoided. So it is ideal to vale validations at 3 levels. It becomes a nightmare to manage them. Some times when application wants to skip some validations the validations set at database level doesn't allow that. Having such a scenario has another issue which is data inconsistency.
- At DB level write indexes, unique_indexes and foreign keys to bac k up the validations set on application.

- Avoid n+1 queries. data driven coding.

- Avoid Hardcoding data.

- inside a method or function, dont depend on values which are fetched from outside service called inside the method/function description. Unless the whole job of the method is to fetch the value. In case of a method, either the values has to come from the object the method is defined in, or should be passed as a parameter. In case of a function, only way the data can reach the function is via parameters. (Blocks in ruby are also fine). If we are fetching any other details using a service from inside a function, it is a tight dependancy and makes it hard to test. As mentioned, unless the methods only task is to fetch the data.
	- Downside is, injecting a data accross methods from outside becomes impossible. any such project wide change will require editing each method call to include the new data addition. eg: if we started having a global User object for a session, and each method now has to respect it. When each method definition is edited, we will have to edit the method calls to pass this global User object.


#### Uploading to CDN

When uploading to CDN,  and storing the reference in local database.
Ensure the CDN credentials are nested and uniquely identified.
Be careful around crential change. Life if you are changing the Azure bucket name,
but your old files are still in old bucket, keep the relationship intact. Identify each file with itse set of credentials for future download.

#### Database

- always maintain audit trail of each actions.
- do soft delete - never hard delete.
