[Index](index.md)

---

## What is your approach to developing a code that is maintainable in a long term?

- Encapsulations: For every action create a separate method. Do not define an action in a combination method. Instead have separate methods for each action, then collect them to act in group using pipeline methods. - Single responsibility principle + pipeline methods.
Eg: If you have to create and send a PDF. One method for creating PDF, another method for sending of PDF or even generic method sending any file with address and sender details as parameters. A method to collect these two methods to run in series, as a pipeline. That way we can use PDF generator for another use case as saving of PDF to storage. We can use the send email for sending other documents as well.

- Test Driven Development. Write Tests. Both Unit and Integration.

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

- Write validations at 3 levels. Front end, back end and database level. Most applications reduce the validations to backend level. Not bad. But the best way to ensure uniqueness validation is at database level. if database provide atomic operations use that. Some are lazy and l put validations at front end alone. That should be avoided. So it is ideal to vale validations at 3 levels. It becomes a nightmare to manage them. Some times when application wants to skip some validations the validations set at database level doesn't allow that. Having such a scenario has another issue which is data inconsistency.

- Avoid n+1 queries. data driven coding.

- Avoid Hardcoding data.
