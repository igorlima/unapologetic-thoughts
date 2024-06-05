---
layout: post
title: Python module argparse
category: code-sample
---

The `argparse` module in Python!

`argparse` is a built-in Python module that makes it easy to write user-friendly command-line interfaces (CLIs) for your scripts and programs. It allows you to define command-line arguments, options, and subcommands, and automatically generates help messages and usage texts.

Here are some key features and benefits of using `argparse`:

**Key Features:**

1. **Argument parsing**: `argparse` can parse command-line arguments, including options, flags, and positional arguments.
2. **Option specification**: You can define options with short and long names, default values, and help texts.
3. **Subcommands**: `argparse` supports subcommands, which allow you to create complex command-line interfaces with multiple commands.
4. **Help and usage messages**: `argparse` automatically generates help and usage messages based on your option and argument definitions.
5. **Error handling**: `argparse` provides built-in error handling for invalid arguments, options, and subcommands.

**Benefits:**

1. **Easy to use**: `argparse` is a simple and intuitive module to use, even for complex command-line interfaces.
2. **Flexible**: You can define custom options, arguments, and subcommands to fit your specific needs.
3. **Consistent**: `argparse` ensures consistency in your command-line interface, making it easier for users to understand and use.
4. **Portable**: `argparse` is a built-in Python module, so you don't need to worry about dependencies or compatibility issues.

**Basic Example:**

```python
import argparse

parser = argparse.ArgumentParser(description='My script')
parser.add_argument('--foo', help=' Foo option')
parser.add_argument('bar', help='Bar argument')

args = parser.parse_args()
print(args.foo, args.bar)
```
In this example, we create an `ArgumentParser` object and define two arguments: `--foo` (an option) and `bar` (a positional argument). We then parse the command-line arguments using `parse_args()` and print the values of `foo` and `bar`.

**Advanced Features:**

1. **Mutually exclusive groups**: You can define groups of options that are mutually exclusive, meaning only one option in the group can be specified.
2. **Subparsers**: `argparse` supports subparsers, which allow you to create subcommands with their own options and arguments.
3. **Custom actions**: You can define custom actions to perform when an option or argument is specified.
4. **Argument validation**: `argparse` provides built-in validation for arguments, such as checking if a value is a valid integer or file path.

Overall, `argparse` is a powerful and flexible module that makes it easy to create user-friendly command-line interfaces for your Python scripts and programs.

<details markdown="block">
<summary><i>code sample <code>args.py</code></i></summary>

```python
import argparse, sys

"""
- https://docs.python.org/3/library/argparse.html
  - https://docs.python.org/pt-br/3/library/argparse.html
- https://docs.python.org/3.7/library/argparse.html
  - https://docs.python.org/pt-br/3.7/library/argparse.html
"""

# argparse
parser = argparse.ArgumentParser(
  description='Search and retrieve with RRF and vector search'
)
parser.add_argument('-q', '--query', help='Query with RRF search')
parser.add_argument('-r', '--retriever', help='Retrieve with RRF retriever')
parser.add_argument('-v', '--vector', help='Query with vector search')

# main
def main():
  # args
  args = parser.parse_args()

  # query
  if args.query:
    print('Query:', args.query)
  elif args.retriever:
    print('Retriever:', args.retriever)
    sys.exit(0)
  elif args.vector:
    print('Vector:', args.vector)
  else:
    sys.exit(0)

  print('---')

if __name__ == '__main__':
    main()
```
</details>


---
{: data-content="footnotes"}

[^1]: [...]({{site.baseurl}}{% post_url 2023/2023-03-30-internal-links %})
[^2]: [...]({{site.baseurl}}{% link editable.html %})
