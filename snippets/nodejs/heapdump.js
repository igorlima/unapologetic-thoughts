/*
 npm --prefix package/heapdump run
 npm --prefix package/heapdump start
 npm --prefix package/heapdump init
 npm --prefix package/heapdump ci
 npm --prefix package/heapdump install express --save
 */
const v8 = require("v8");
const express = require("./package/heapdump/node_modules/express");
const app = express();
const PORT = 3000;

const headersArray = [];
app.get("/", (req, res) => {
  headersArray.push({ userAgentUsed: req.get("User-Agent") });
  res.status(200).send(JSON.stringify(headersArray));
});

process.on('SIGUSR2', () => {
  const fileName = v8.writeHeapSnapshot();
  console.log(`Created heapdump file: ${fileName}`);
});

app.listen(PORT, () => {
  console.log(`Server listening on http://localhost:${PORT}/`);
});

/*
 HOW TO RUN THE CODE
 ```sh
 lsof -i :3000
 kill -SIGUSR2 <the_process_id>
 ```

REFERENCES:
• Preventing and Debugging Memory Leaks in Node.js
  - https://betterstack.com/community/guides/scaling-nodejs/high-performance-nodejs/nodejs-memory-leaks/
*/

