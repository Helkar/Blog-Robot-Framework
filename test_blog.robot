*** Settings ***
Documentation  My Ruby on Rails Blog tests
...
Library  blog.BlogHomePage
Library  blog.BlogPostPage
Library  blog.BlogEditPostPage
*** Test Cases ***

When a user adds a new post, it should be shown and it can be deleted
    Open Blog
    Click in New Post
    Type in Title Box   Testing 
    Type in Body Box    Hello World by evialva
    Click in Create Post
    Blog Post Page Body Should Contain     Post was successfully created
    Click in Back
    Blog Body Should Contain         Testing
    Click in Destroy                 Testing    Hello World by evialva
    Blog Body Should Not Contain     Testing
    [Teardown]  Close Blog

When a user tries to add a new post, title and body are mandatory
    Open Blog
    Click in New Post
    Click in Create Post
    Blog Post Page Body Should Contain     Title can't be blank
    Blog Post Page Body Should Contain     Body can't be blank
    [Teardown]  Close Blog Post Page

When a user tries to add a new post, title is mandatory
    Open Blog
    Click in New Post
    Type in Body Box    Hello World by evialva
    Click in Create Post
    Blog Post Page Body Should Contain     Title can't be blank
    [Teardown]  Close Blog Post Page

When a user tries to add a new post, body is mandatory
    Open Blog
    Click in New Post
    Type in Title Box    Holaaaa
    Click in Create Post
    Blog Post Page Body Should Contain     Body can't be blank
    [Teardown]  Close Blog Post Page

When a user adds a new post, a comment can be added
    Open Blog
    Click in New Post
    Type in Title Box   Stargate
    Type in Body Box    SG-1
    Click in Create Post
    Blog Post Page Body Should Contain     Post was successfully created
    Type in Comment Box     Stargate Rules!
    Click in Add Comment
    Blog Post Page Body Should Contain          Stargate Rules!
    Click in Back
    Blog Body Should Contain         Stargate
    Click in Destroy                 Stargate    SG-1
    Blog Body Should Not Contain     Stargate
    [Teardown]  Close Blog

When a user adds a new post, it can be edited
    Open Blog
    Click in New Post
    Type in Title Box   Farscape
    Type in Body Box    Moya
    Click in Create Post
    Blog Post Page Body Should Contain     Post was successfully created
    Click in Back
    Blog Body Should Contain         Farscape
    Click in Edit       Farscape    Moya
    Edit Title Box                   arg
    Click in Update Post 
    Blog Body Should Contain         arg
    Click in Back
    Click in Destroy                 arg    Moya
    Blog Body Should Not Contain     arg
    [Teardown]  Close Blog

