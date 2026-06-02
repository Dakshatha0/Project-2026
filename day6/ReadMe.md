* Authentication is the process by which a system authenticates a user.
    - Examples: Username/Password, MFA, SSO, Token-based authentication
* Authorization:
    - Authentication is a prerequisite to authorization. Once the system authenticates a user, it must decide whether the user can access certain features, data, or functionality. 
* Stateful authentication keeps track of user login sessions on the server side (e.g., in a database or server memory). 
* Stateless authentication relies on cryptographically signed tokens (like JWTs) sent by the client, meaning the server stores no session data and treats every request independently.
* API keys act as unique identifiers that grant access rights to specific resources or services provided by an application programming interface (API).
* OAuth, which stands for Open Authorization, is a widely used authorization framework that enables applications to obtain limited access to user accounts on an HTTP service, such as Facebook, GitHub, or Google. It’s designed to work over HTTPS and allows applications to authenticate a user without accessing their password. Instead, OAuth uses access tokens to prove an authorization decision.

Resources:
    - https://rakiabensassi.medium.com/authentication-authorization-11b8078b4bdf
    - https://medium.com/@devnabibia/authentication-and-authorization-concepts-you-must-know-38bd9c367ec0
    - https://medium.com/@pollywops2015/api-keys-the-definitive-guide-to-understanding-them-23934aa8061a
    - https://medium.com/@shwetakoffficiall/access-token-and-refresh-token-in-authentication-and-auth-in-simple-way-d5ac44a9750f
    - https://medium.com/@shankarvarat_86560/what-is-oauth-d02f854579a9
    - https://windmaomao.medium.com/oauth-explained-in-simple-words-part-i-2423dad857fc