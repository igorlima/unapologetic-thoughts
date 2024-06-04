---
layout: post
title: JS - waitFor function
category: code-sample
---

Here's an improved version of your text, with a friendly and positive tone:

The `waitFor` function below is designed to take two timeout values as optional parameters. The first timeout is for the repeated attempts to check a certain condition. The second timeout is for the entire function, and if it exceeds this limit, the function will fail.

The `waitFor` function returns a promise that will resolve when the specified condition is met or reject when the timeout is reached.

Additionally, there is another version of the `waitFor` function that accepts a callback function as a parameter instead of returning a promise. This callback function is called when either the condition is met or the timeout is reached. When the condition is met, the callback function is passed a boolean value of `true`. When the timeout is reached, the callback function is passed a boolean value of `false`.

<details markdown="block">
<summary><i>function <code>waitFor</code></i></summary>

```js
const _waitFor = (conditionFn, callback, options) => {
  const {timeoutRetry = 100, timeout = 2000, ID = {
    timeoutRetry: [],
    timeout: []
  }} = options || {}
  const clearAllTimeouts = () => Object.values(ID).forEach(ids => {
    ids.forEach(id => clearTimeout(id))
  })
  if (conditionFn()) {
    clearAllTimeouts()
    callback(true)
    return
  }
  ID.timeoutRetry.push(setTimeout(() => {
    _waitFor(conditionFn, callback, Object.assign(options || {}, {ID}))
  }, timeoutRetry))
  ID.timeout.push(setTimeout(() => {
    clearAllTimeouts()
    callback(false)
  }, timeout))
}

const waitFor = (conditionFn, options) => new Promise((resolve, reject) => {
  _waitFor(conditionFn, (bool) => {
    return bool ? resolve(bool) : reject(bool)
  }, options)
})
```
</details>

<details markdown="block">
<summary><i>for testing...</i></summary>

```js
_waitFor(() => {
  console.log('.')
  return false
}, (bool) => {
  console.debug(bool)
  debugger
}, {timeoutRetry: 50, timeout: 3000})

waitFor(() => {
  return false
}, {timeoutRetry: 50, timeout: 3000}).then((bool) => {
  console.debug(`OK: ${bool}`)
  debugger
}).catch((bool) => {
  console.debug(`FAIL due to waiting too much: ${bool}`)
  debugger
})

A = false
setTimeout(() => A = true, 1000)
waitFor(() => {
  return A
}, {timeoutRetry: 50, timeout: 3000}).then((bool) => {
  console.debug(`OK: ${bool}`)
  debugger
}).catch((bool) => {
  console.debug(`FAIL due to waiting too much: ${bool}`)
  debugger
})
```
</details>

---
{: data-content="footnotes"}

[^1]: [...](...)
