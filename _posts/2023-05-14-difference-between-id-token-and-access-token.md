---
layout: post
title: difference between id token and access token
category: technical
---

_ID Token and Access Token: What Is the Difference?_ [^1]

_Should I use the ID token or the access token?_
In the case of ID and access tokens, they have clear and well- defined purposes.
Using the wrong token can result in your solution being insecure.

_What Is an ID Token?_
An ID token is an artifact that proves that the user has been authenticated.
ID token is a proof of the user's authentication.
An ID token is encoded as a JSON Web Token (JWT), a standard format that allows your application to easily inspect its content, and make sure it comes from the expected issuer and that no one else changed it.
The ID token is not encrypted but just Base 64 encoded. 
First, it demonstrates that the user has been authenticated by an entity you trust (the OpenID provider) and so you can trust the claims about their identity.

_What Is an Access Token?_
The access token is the artifact that allows the client application to access the user's resource.
In the OAuth 2 context, the access token __allows a client application to access a specific resource to perform specific actions on behalf of the user__.
Scopes are a mechanism that allows the user to authorize a third-party application to perform only specific operations.

_What Is It NOT Suitable For?_
ID token will not have granted scopes (I know, this is another pain point). As said before, scopes allow the user to restrict the operations your client application can do on their behalf. Those scopes are associated with the access token so that your API knows what the client application can do and what it can't do.
The access token should not be inspected by the client application.


![image](https://github.com/igorlima/unapologetic-thoughts/assets/1886786/79a644a8-27f0-4c14-8aa7-e47a0f5f52d7)


---
{: data-content="footnotes"}

[^1]: [ID Token and Access Token: What's the Difference?](https://auth0.com/blog/id-token-access-token-what-is-the-difference/)
