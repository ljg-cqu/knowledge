Say I have a native Swift app running on macOS, which receives and runs Python code provided by users from the UI. How can my app run Python directly? Which approach is the simplest and most stable?

Mon Jul 21 2025

Your native Swift macOS app can run user-provided Python code directly by embedding a Python interpreter using PythonKit or by running Python scripts as separate processes via NSTask or Process APIs. Among these, embedding Python using PythonKit is generally the simplest and most stable approach, offering seamless Swift-Python interoperability within your app.

### Approaches to Running Python Code in a Swift macOS App

#### 1. Embedding Python Interpreter Using PythonKit

PythonKit is a Swift framework that bridges Swift and Python, allowing you to run Python code and import Python modules directly from Swift code. This approach embeds a Python interpreter into your app, enabling direct and efficient Python execution.

- **Setup**: Add PythonKit as a Swift Package Manager dependency in your Xcode project.
- **Embedding Python Runtime**: You need to bundle the Python runtime with your app, ideally using a Python framework like `Python-Apple-support`, which provides a ready-to-use Python stdlib and dynamic libraries for macOS.
- **Initializing Python**: At runtime, set environment variables `PYTHONHOME` and `PYTHONPATH` to point to the embedded Python resources.
- **Executing Python**: Use PythonKit APIs to import Python modules and call Python functions right from Swift.
- **Advantages**:
  - Seamless integration with Swift, no need to spawn external processes.
  - Enables direct data exchange between Swift and Python types.
  - Supports complex Python libraries and user-provided scripts reliably.
- **Considerations**:
  - Increases app binary size (~100MB for embedding Python).
  - Requires code signing and proper entitlements for macOS App Store submission.
- **Example**:
  ```swift
  import PythonKit
  let sys = Python.import("sys")
  print("Python version: \\(sys.version)")
  let math = Python.import("math")
  print("cos(1) = \\(math.cos(1))")
  ```
- **References**: Embedding Python using PythonKit and `Python-Apple-support`, with detailed build and signing steps.

#### 2. Running Python Scripts as Separate Processes

If embedding an interpreter is undesired, your app can run Python scripts as external processes using `Process` (formerly `NSTask`):

- **Packaging**: Bundle user-provided Python scripts or pre-packaged Python apps (e.g., created by PyInstaller) inside your app’s resources.
- **Execution**: Use the `Process` API to launch the system’s Python interpreter or the bundled Python app, passing the script path and any arguments.
- **Output Handling**: Capture standard output and error streams to retrieve execution results.
- **Example**:
  ```swift
  let process = Process()
  process.executableURL = URL(fileURLWithPath: "/usr/bin/python3")
  process.arguments =
  let pipe = Pipe()
  process.standardOutput = pipe
  try process.run()
  process.waitUntilExit()
  let data = pipe.fileHandleForReading.readDataToEndOfFile()
  let output = String(data: data, encoding: .utf8)
  print(output ?? "No output")
  ```
- **Advantages**:
  - Simpler to implement initially.
  - Avoids increasing app size by embedding Python.
- **Considerations**:
  - Python environment must be available on the user’s system unless you bundle it.
  - Running external processes is less tightly integrated and may require inter-process communication.
  - Debugging and error handling add complexity.
- **Additional Tips**:
  - Using PyInstaller, bundle Python scripts as `.app` and include them in the main app bundle.
  - Launch these bundled apps with `NSWorkspace.shared.launchApplication(at:)`.
- **References**: Detailed PyInstaller packaging and external process launching steps.

#### 3. Using System Command Execution via `posix_spawn` or `NSTask`

- `Process` uses underlying `posix_spawn` to run commands; this is mostly transparent to you.
- Advanced techniques allow spawning subprocesses with custom input/output pipes.
- For user input and more complex subprocess interactions, Swift's newer `Subprocess` APIs (introduced in recent Foundation versions) provide a robust alternative.

### Recommended Approach

For your use case—running user-provided Python code from your macOS Swift app UI—the **simplest and most stable** approach is to **embed Python using PythonKit**. This method simplifies execution flow, avoids dependency on the user’s system Python, and provides rich interoperability, enhancing your app's capability to directly invoke Python code and libraries seamlessly,,.

If app size or complexity is a concern, or you prefer isolating Python execution, running Python as an external process (packaged with PyInstaller) is a viable alternative, though it introduces more complexity in managing subprocesses and inter-process communication.

### Summary

| Approach                         | Pros                                        | Cons                                         |
|---------------------------------|---------------------------------------------|----------------------------------------------|
| PythonKit embedding              | Seamless integration, direct calls, rich API | Larger app size, requires embedding & signing |
| Running Python as external process | Simpler initially, smaller app size          | Requires Python environment/bundling, less integrated |
| System command execution (posix_spawn/NSTask) | Fine control of subprocesses                  | Complex for input/output management, sandbox limitations on macOS |

In conclusion, embedding Python with PythonKit is the most straightforward, robust way to execute user-provided Python code inside a native Swift macOS app. It offers a stable and maintainable solution for mixed Swift-Python workflows.

Bibliography
7. Using Python on iOS — Python 3.13.5 documentation. (n.d.). https://docs.python.org/3/using/ios.html

Add support for posix_spawn call in subprocess.Popen with ... - GitHub. (2023). https://github.com/python/cpython/issues/113117

Building and Running Python Scripts with Xcode 6.1 | Vandad NP. (2014). https://vandadnp.wordpress.com/2014/10/20/building-and-running-python-scripts-with-xcode-6-1/

Call Python code from an existing project written in Swift. (2015). https://stackoverflow.com/questions/31927604/call-python-code-from-an-existing-project-written-in-swift

Calling Python Scripts from Swift by PythonKit. - MLBoy - Medium. (2020). https://rockyshikoku.medium.com/calling-python-scripts-from-swift-by-pythonkit-faf41757e890

Can you run a python script in Swift based app? - Reddit. (2022). https://www.reddit.com/r/iOSProgramming/comments/ys3d5b/can_you_run_a_python_script_in_swift_based_app/

Easy way to Package and Run Python in Swift - Stackademic. (2023). https://blog.stackademic.com/easy-way-to-package-and-run-python-in-swift-2b7e6b9cb6a2

Embedding a Python interpreter inside a MacOS / iOS app ... - Medium. (2022). https://medium.com/swift2go/embedding-python-interpreter-inside-a-macos-app-and-publish-to-app-store-successfully-309be9fb96a5

Embedding Python interpreter inside a MacOS app (and iOS app ... (2022). https://dev.to/eldare/embedding-python-interpreter-inside-a-macos-app-and-publish-to-the-app-store-successfully-4bop

Getting Started with PythonKit. (n.d.). https://noumenal.es/notes/til/swift/starting-python-kit/

How do you run python script with arguments programmatically ... (2020). https://www.reddit.com/r/macprogramming/comments/fj6kf4/how_do_you_run_python_script_with_arguments/

How do you use posix_spawn to replace the deprecated “system” to ... (2014). https://stackoverflow.com/questions/27046728/how-do-you-use-posix-spawn-to-replace-the-deprecated-system-to-launch-opendiff/47169872

How to allow `Process` to receive user input when run as part of an ... (2020). https://forums.swift.org/t/how-to-allow-process-to-receive-user-input-when-run-as-part-of-an-executable-e-g-to-enabled-sudo-commands/34357/3

How to Run a Python Script in macOS App | by Rohit Saini - Medium. (2024). https://medium.com/codex/how-to-run-a-python-script-in-macos-app-4166eae4d083

How to run python program in IOS Swift app - Stack Overflow. (2017). https://stackoverflow.com/questions/46657162/how-to-run-python-program-in-ios-swift-app

I need to execute a python script via NSTask from a macOS app, but ... (2020). https://stackoverflow.com/questions/63016349/i-need-to-execute-a-python-script-via-nstask-from-a-macos-app-but-the-script-ca

import python to Xcode | Apple Developer Forums. (2021). https://developer.apple.com/forums/thread/697648

Issue 35537: use os.posix_spawn in subprocess - Python tracker. (2018). https://bugs.python.org/issue35537

johnno1962/YieldGenerator: Python’s “yield” generators for Swift. (2015). https://github.com/johnno1962/YieldGenerator

Loading Python Runtimes in Swift - Medium. (2020). https://medium.com/red-teaming-with-a-blue-team-mentality/loading-python-runtimes-in-swift-20648890489c

NSTask Tutorial for OS X - Kodeco. (2016). https://www.kodeco.com/1197-nstask-tutorial-for-os-x

pvieito/PythonKit: Swift framework to interact with Python. - GitHub. (n.d.). https://github.com/pvieito/PythonKit

Python interop with PythonKit - Using Swift. (2019). https://forums.swift.org/t/python-interop-with-pythonkit/28386

PythonKit integration with Swift - Crashing on release due to module ... (2024). https://forums.swift.org/t/pythonkit-integration-with-swift-crashing-on-release-due-to-module-import/72770

r0ml/Caerbannog: Swift Package to embed Python into a macOS app. (n.d.). https://github.com/r0ml/Caerbannog

[Review] SF-0007: Introducing Swift Subprocess - Page 6 - Foundation. (2024). https://forums.swift.org/t/review-sf-0007-introducing-swift-subprocess/70337?page=6

Run Python Script in an iOS app Sw… | Apple Developer Forums. (2016). https://developer.apple.com/forums/thread/63313

Running a script from within swift app (QLExtension). (2024). https://forums.swift.org/t/running-a-script-from-within-swift-app-qlextension/70226

swift - Use of posix_spawn? - Stack Overflow. (2016). https://stackoverflow.com/questions/39511050/use-of-posix-spawn

There is a problem launching using posix_spawn (error code: 8). (2024). https://discussions.apple.com/thread/255573154

Using Task on Linux - Swift Forums. (2017). https://forums.swift.org/t/using-task-on-linux/4843

Why no pointers to Swift documentation for interacting with the server. (2016). https://www.couchbase.com/forums/t/why-no-pointers-to-swift-documentation-for-interacting-with-the-server/8448

Xcode Python: The Ultimate Development Environment for Python ... (2025). https://www.browserstack.com/guide/xcode-python-guide



Generated by Liner
https://getliner.com/search/s/5926611/t/86708135

---

With embedded PythonKit, users only need to start one app, eliminating the need for a separate process. Right?

Yes. With embedded PythonKit, the Python interpreter runs inside your Swift app as a single integrated process, so no separate Python process needs to be started.

Embedded PythonKit Runs Python Inside a Single App Process

    When using PythonKit to embed Python in your macOS Swift app, the Python interpreter is initialized and lives within the same application process. Your app starts one executable, and Python runs as an embedded interpreter inside that process, eliminating the need to launch or manage external Python processes separately.

    - The integrated approach initializes the Python interpreter runtime at app startup or on demand, allowing Python scripts and modules to execute directly in-process.
- This means user-provided Python code is executed within the main app’s process space, enabling fast and seamless Swift-Python interaction without process boundaries.
- The embedded interpreter shares the same memory and runtime environment, which simplifies data sharing and avoids overhead and complexity of inter-process communication required if Python ran externally.

  Benefits of Single-Process Embedding with PythonKit

  Simplifies app deployment and execution**: Users only need to launch your single native app.
  Performance**: No costly process spawning or IPC delays.
  Stability**: Avoids process management issues with external Python interpreters.
  App Store Compliance**: Having all runtime integrated avoids sandboxing and runtime environment restrictions linked with launching external processes.

  In short, embedded PythonKit makes your macOS app self-contained with Python runtime inside one single app process, requiring no extra standalone Python process execution by the user. This is one of the core advantages of embedding Python via PythonKit.

Sources:
[1] Embedded Python — kit-manual 104.0 documentation, https://docs.omniverse.nvidia.com/kit/docs/kit-manual/104.0/guide/embedded_kit_python.html
[2] 1. Embedding Python in Another Application — Python 3.13.5 ..., https://docs.python.org/3/extending/embedding.html
[3] Embedding a Python interpreter inside a MacOS / iOS app ... - Medium, https://medium.com/swift2go/embedding-python-interpreter-inside-a-macos-app-and-publish-to-app-store-successfully-309be9fb96a5
[4] Embedding Python interpreter inside a MacOS app (and iOS app ..., https://dev.to/eldare/embedding-python-interpreter-inside-a-macos-app-and-publish-to-the-app-store-successfully-4bop
[5] Creating macOS Apps Using Python and PythonKit - Medium, https://medium.com/codex/creating-macos-apps-using-python-and-pythonkit-825f9c446e49
[6] PythonKit not linking? - Related Projects - Swift Forums, https://forums.swift.org/t/pythonkit-not-linking/62459
[7] Getting Started with PythonKit, https://noumenal.es/notes/til/swift/starting-python-kit/
[8] Quick question can app using python kit get published to macOS ..., https://groups.google.com/a/tensorflow.org/g/swift/c/yAzJFMYRkF8
[9] Using PythonKit in multi-threaded application - Swift Forums, https://forums.swift.org/t/using-pythonkit-in-multi-threaded-application/55155
[10] From Swift Import Python. Build a macOS app to run Python scripts…, https://anupamchugh.medium.com/from-swift-import-python-f2fc2a997d4
[11] PythonKit for OSX Swift project suddenly not finding modules, https://stackoverflow.com/questions/67022843/pythonkit-for-osx-swift-project-suddenly-not-finding-modules
[12] How to implement Python into Xcode using pythonkit 3rd party ..., https://forums.swift.org/t/how-to-implement-python-into-xcode-using-pythonkit-3rd-party-software-or-any-others-please-suggest/32319
[13] pvieito/PythonKit: Swift framework to interact with Python. - GitHub, https://github.com/pvieito/PythonKit
[14] 7. Using Python on iOS — Python 3.13.5 documentation, https://docs.python.org/3/using/ios.html
[15] Testing Extensions with Python — kit-manual 104.0 documentation, https://docs.omniverse.nvidia.com/kit/docs/kit-manual/104.0/guide/testing_exts_python.html
[16] PythonKit error "Python library not found. Set the ... - Stack Overflow, https://stackoverflow.com/questions/60080176/pythonkit-error-python-library-not-found-set-the-python-library-environment-va
[17] Calling a python Command-line tool with arguments, with PythonKit ..., https://stackoverflow.com/questions/72527890/calling-a-python-command-line-tool-with-arguments-with-pythonkit-using-swift
[18] Using the manual installation (without briefcase), is there any way to ..., https://github.com/beeware/Python-Apple-support/issues/175
[19] I can't import Python modules in Xcode 11 using PythonKit, https://stackoverflow.com/questions/57126337/i-cant-import-python-modules-in-xcode-11-using-pythonkit
[20] Bundle python + 3rd party packages to macOS app - Reddit, https://www.reddit.com/r/Python/comments/1kzkmtl/bundle_python_3rd_party_packages_to_macos_app/
