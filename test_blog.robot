*** Settings ***
Documentation     My Ruby on Rails Blog tests
Library           blog.BlogHomePage
Library           blog.BlogNewPostPage
Library           blog.BlogEditPostPage
Library           blog.BlogShowPostPage
Resource          resource.txt

*** Test Cases ***
When a user adds a new post, it should be shown and it can be deleted
    [Tags]    Critical
    [Setup]    Open Blog
    Create Post    ${POST TITLE1}    ${POST BODY1}
    Click in Back
    Blog Body Should Contain    ${POST TITLE1}
    Click in Destroy    ${POST TITLE1}    ${POST BODY1}
    Blog Body Should Not Contain    ${POST TITLE1}
    [Teardown]    Close Blog

When a user tries to add a new post, title and body are mandatory
    [Setup]    Open Blog
    Click in New Post
    Click in Create Post
    Blog New Post Page Body Should Contain    Title can't be blank
    Blog New Post Page Body Should Contain    Body can't be blank
    [Teardown]    Close Blog New Post Page

When a user tries to add a new post, title is mandatory
    [Setup]    Open Blog
    Click in New Post
    Type in Body Box    ${POST BODY1}
    Click in Create Post
    Blog New Post Page Body Should Contain    Title can't be blank
    [Teardown]    Close Blog New Post Page

When a user tries to add a new post, body is mandatory
    [Setup]    Open Blog
    Click in New Post
    Type in Title Box    ${POST TITLE1}
    Click in Create Post
    Blog New Post Page Body Should Contain    Body can't be blank
    [Teardown]    Close Blog New Post Page

When a user adds a new post, a comment can be added
    [Setup]    Open Blog
    Create Post    ${POST TITLE2}    ${POST BODY2}
    Type in Comment Box    ${POST COMMENT}
    Click in Add Comment
    Blog Show Post Page Comment Should Contain    ${POST TITLE2}    ${POST BODY2}    ${POST COMMENT}
    Click in Back
    Blog Body Should Contain    ${POST BODY2}
    Click in Destroy    ${POST TITLE2}    ${POST BODY2}
    Blog Body Should Not Contain    ${POST TITLE2}
    [Teardown]    Close Blog

When a user adds a new post, it can be edited
    [Setup]    Open Blog
    Create Post    ${POST TITLE3}    ${POST BODY3}
    Click in Edit    ${POST TITLE3}    ${POST BODY3}
    Edit Title Box    arg
    Click in Update Post
    Blog Show Post Page Body Should Contain    arg
    Click in Back
    Click in Destroy    arg    ${POST BODY3}
    Blog Body Should Not Contain    ${POST BODY3}
    [Teardown]    Close Blog

When a user adds a new post, it can be showed
    [Setup]    Open Blog
    Create Post    ${POST TITLE4}    ${POST BODY4}
    Click in Back
    Blog Body Should Contain    ${POST TITLE4}
    Click in Show    ${POST TITLE4}    ${POST BODY4}
    Blog Body Should Contain    ${POST BODY4}
    Click in Back
    Click in Destroy    ${POST TITLE4}    ${POST BODY4}
    Blog Body Should Not Contain    ${POST TITLE4}
    [Teardown]    Close Blog

*** Keywords ***
Create Post
    [Arguments]    ${title}    ${body}
    Click in New Post
    Type in Title Box    ${title}
    Type in Body Box    ${body}
    Click in Create Post
    Blog Show Post Page Body Should Contain    Post was successfully created
