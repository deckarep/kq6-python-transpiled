# Script Transpiler (by deckarep)

First of all, the Python3 transpiler is built on top (read: kinda-hacked onto) sluicebox's huge body of work. Most of the hardwork was done by him
to unleash a decompiler that as far as I can tell and tested, is damn near complete. This work wouldn't exist without his hard work
and therefore most of the credit goes to him as well as those who came before him with respect to SCI reverse engineering. Please read
the Tools (next section below) by sluicebox for context on his original decompiler work.

With that said, can we convert Sierra's SCI Script into something runnable and is it even remotely possible?

* Step 1: Transpile SCI Script to Python3
* Step 2: Build the game engine + kernel layer
* Step 3: Play a game and profit

See, it's easy right? No, not really but let's break this down.

* First transpile SCI Script => Python3
  * Lose the SCI/Lisp/SmallTalk S-Expression syntax (thanks but no thanks [Jeff Stephenson](https://sierra.fandom.com/wiki/Jeff_Stephenson))
    * Convert SmallTalk influenced cascade syntax to a simulated syntax (squint your eyes) that Python3 supports.
      * Quick Review:
        * Object: Some in-memory entity that has zero or more properties and zero or more methods
        * Selector: Can either be a "method" or a "property" on the object.
        * Send: The runtime dispatching of setting a property, reading a property or invoking a method.
          * Set a property: `(ego x: 32)`
          * Get a property: `(ego x)`
          * Invoke a method: `(ego setCycler: Fwd)`
          * You can even do a bunch of these operations in a single `send` cascade.
      * Mimic cascade/send syntax in Python3
        * Ex: `(ego x:32 setCycler: Fwd doCalc: 1 2 3)` => `ego._send('x:', 32, 'setCycler': Fwd, 'doCalc:', 1, 2, 3)`
    * Convert prefix notation to infix like every other goddamn modern language
      * Ex: `(+ 4 4)` => `4 + 4` or `(or param1 5)` => `param1 or 5`
      * Ex: n-array: `(* 3 2 10)` => `3 * 2 * 10`
    * Convert SCI `(cond ...)` statements to Python3 `if/elif/else` chains
    * Convert SCI `(switch ...)` statements to Python3 pattern match-style statements
    * Convert SCI if expressions into Python3 ternary expressions.
      * Ex: `(if (== param1 40) 1 else 0)` => `1 if param1 == 40 else 0`
  * Find and deprecate all uses of `@ (AddressOf)` operator
    * This was primarily used in SCI to manipulate strings and arrays without having to do expensive copies
    * Going forward, we likely won't even need this but a deeper dive needs to be done as we practically get this for free in Python
  * Convert SCI hex format: `$8000` => Python3 hex format: `0x8000`
  * Convert SCI verbatim strings `{JOLLO}` to Python3 verbatim strings `r"""JOLLO"""`
  * Convert SCI array syntax: `[myArray0 5] = [0 1 2 3 4]` to Python3 lists `myArray0 = [0, 1, 2, 3, 4]`
    * Declaration only form: `[myArray0 5]` => `myArray = [0] * 5` which creates an array size of 5 that is zeroed out
  * Ensure any and all `assignment expressions` use the Python3 walrus operator `:=`
  * For functions/procs that use introspect arguments with `argc` emit a local variable of the count of all passed-in parameters
  * Rewrite all increment `++` and decrement `--` expressions as `val.inc()` or `val.dec()`. NOTE: This requires an `Int16`  wrapping class, so please read below.
  * Ensure all memory-based free functions set fields to `None` so Python3 GC kicks in and no leaks are created
  * Ensure empty methods or procs are preserved but use the Python3 `pass` statement for the body
* Bootstrap a kernel/game engine
  * Model this off of ScummVM's implementation
  * Or use ScummVM's implementation directly and rip out the SCI Virtual Machine and replace with the Python3 runtime.
  * Also I already have [a rudimentary engine working running Python3 SCI](https://youtu.be/P1D0cdzexy4) see here!

* Python3 abitrary precision numbers
  * [See this for a Int16 wrapper class](https://gist.github.com/deckarep/23d90ce44cfdfc89f89865b5582dc178) example (NOT FINAL)
  * Since Python3 numbers know no bounds and can support abitrary precision numbers including decimals this won't
    quite work for us with respect to supporting an SCI transpiled port. The reason is because SCI ONLY ever supports
    Int16 or Int32 signed values and there is no room for anything else. Anything else will create bugs.
  * How to handle this
    * Implement an Int16/i16 wrapper class that has all the necessary Python meta-methods for overloading
    * Additionally, during transpile ensure all declared arrays, properties, etc are typed using this wrapper class
      * Ex: `register = i16(0)` during initialization.
    * Additionally, ensure that ALL assign statements AND assign expressions that are number based also wrap the RHS
      * Ex: `register = i16(3 * 4)`
      * Ex: `if register := i16(4 + ego.x): ...` notice the walurus operator as this is an assign expression
  * This wrapper class will ensure all computations are masked with: `0xffff` to keep everythin as Int16 precision
  * Additionally, this class will introduce two bonus methods to represent: `++` and `--` expression handling
    * The transpile will therefore have to rewrite as: `value++` => `value.inc()` which will represent a post increment
    * The same strategy will obviously be used for decrement: `value--` => `value.dec()`
    * A huge bonus for handling this in the int16 wrapping class for `inc()` and `dec()` is it saves us from having
      to rewrite the AST and introduce a bunch of temporary variables and using Python3's `+=` and `-=` instead. This was going to be a rather ugly chore.
    * NOTE: Since these are POST operators the functions will need to capture the current value as old, bump the actual
      value and return the old value.

* What's the point of all of this?
  * Bring Sierra's SCI scripts into the modern era of software where it can continue to be improved, tweaked, played with, enhanced
  * Make it easy to do to remasters, fan spin-offs, enhanced editions, etc
  * Make it easy to run, build, and quickly iterate on any platform
  * Preserve the code in highly readable syntax that is a lot less esoteric
  * Allow bugs to be fixed, assets to easily be swapped out
  * Allow the extension of new SCI class libraries like a TCP/IP, HTTP network lib that unlocks "online play"
  * The possibilies are endless
  * Easily pack/unpack resources: Views, Pics, Wavs, etc into importable/exportable assets using common file formats.

* But don't mess with these games they're classics!
  * Indeed they are and while messing with the games is fun the real point is to offer a robust
    solution to author your own games or do spin-offs using the same assets and/or open sourced game engine.
  * This new SCI Unlocked engine can be a spiritual successor to new adventure games

* But won't the transpiled Python3 code look ugly?
  * I would say that for the most part the code will be quite similar and be very close to the SCI Script.
  * But Python3 doesn't support small-talk style cascade syntax so that will be not as nice potentially.
  * There will be a hell of a lot less visual clutter: mainly paranthesis and ugly prefix notation.
  * We will lose some niceties such as: ++ and -- which will have to expand out.
  * The goal isn't for the most beautiful transpiled Python3 code, but for a complete and robust transpile that preserves all logic

* Why Python?
  * Python is quite expressive, readable and allows for complex behind the scenes manipulation which can help make this all work.
  * The other language that I considered is Dart, because Dart is one of the few modern languages that supports cascade syntax.

* Will Python execute fast enough and compete with the SCI script?
  * Yes, my prototype proves it's plenty fast, plus heavy-handed code is usually off loaded within the kernel layer
  * In fact, SCI itself is implemented in SCI for some things like List handling, this would be buttloads faster if Python handled list processing instead because much of that is implemented within Python's bytecode interpreter as C code
  * I'm not at all worried about this, so why are you? This is a 35+ year old 2D game engine for crying out loud.

# Sierra Creative Interpreter - Tools (by sluicebox)

This repository contains my SCI reverse engineering software.

- Script decompiler
- Script annotators
- Resource parsers

This software generates my [SCI Scripts repository](https://github.com/sluicebox/sci-scripts), fuels my [blog](https://www.benshoof.org/blog/), and funds my [ScummVM work](https://github.com/scummvm/scummvm/commits?author=sluicebox&path=engines/sci).

If you just want to decompile some games, then you can grab the results from [sci-scripts](https://github.com/sluicebox/sci-scripts). I ran the decompiler so you don't have to. But I didn't want to clutter up that collection with demos or fan games or network clients, so if you want to point this decompiler at the fringes, now you can.

If you're writing your own SCI tools or implementations, then you've come to the right place. The parsers are my readable references; they're heavily documented and handle all the versions I've found.

If you're doing your own SCI reverse engineering, then these are powerful tools, but it's hard to say how because I don't know what you're up to. I'll just say that you're a few short nested loops from having programmatic access to every resource in every game in your corpus, or every function in every script, or every bytecode instruction. If you're more interested in the decompiled scripts, then you can use the language parser to query them and add your own annotations.

If instead you want to play with matches while huffing computer science fumes off a non-trivial bytecode decompiler, then whatever search query got you here, well let's just say you nailed it. The decompiler is some of my best work, which is concerning, given that portions are certifiable. And I don't mean the kind that get you a genius grant, but the kind that get you decided on by courts. For example, if the control flow analysis doesn't make sense, try nodding off in the bath while staring at graphviz. If you're anything like me, it'll make perfect sense in the morning. Until you wake up. And don't get me started on the comments, they're so episodic and introspective that I had to register them as a blog. For tax purposes.

These tools are part of my cozy hobby. This repository is not where development takes place, but it is synchronized to stay up to date. I'm publishing this private work in the hopes that it's useful, but please understand that it's not an invitation. Though if I mucked something up, you can try to let me know. Unbridled praise night be fine too, I dunno. Have to try it on, see if it fits.

Thank you for reading the READ ME. If you didn't read it as Philomena Cunk then try again. But hahdur.
