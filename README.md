# SwimmerSploit
SwimmerSploit is a collection of option fluid payloads that can perform mutiple different shell types without having to be recompiled.

---

## Simple Native Compile or Cross Compile Cheat Sheet

---

### C++ 0r C

* Compile C++/C on Linux for Linux

```bash
gcc linux.c -o compiled
g++ linux.cpp -o compiled

make -f MakeFile
```

* Compile C++/C on Linux for Windows

```bash
x86_64-w64-mingw32-gcc hello_world.c -o hi.exe
x86_64-w64-mingw32-g++ hello_world.cpp -o hi.exe

i686-w64-mingw32-gcc hello_world.cpp -o hi.exe
i686-w64-mingw32-g++ hello_world.c -o hi.exe

i686-w64-mingw32-gcc loader.c -lws2_32 -o avbypass.exe

make -f Makefile.win OS_TARGET=win64 CPU_TARGET=x86_64
```

---

### Csharp/C#

```bash
dotnet build
dotnet build solutionfile.sln
```

* Compile Csharp/C# on Linux for Window

```bash
xbuild solution_file.sln # retired
dotnet build -r win-x64 project.csproj

mono-csc revshells.cs -out:runner.exe 
```

---

### Python3

* Compile Python3 on Linux for Linux

```bash
pyinstaller -F python3-code.py
nuitka3 code.py --standalone --onefile 
```

* Compile Python3 on Windows for Window

```bash
pyinstaller -F python3-code.py
```

---

### Nim

* Compile Nim on Linux for Linux

```bash
nim c filename.nim
nim c filename.nim -o:./run.out
```

* Compile on Nim Linux for Window

```bash
min c -d:release -d:mingw --cpu=i386 project.nim 
min c -d:release -d:mingw --cpu=amd64 -o:./run.exe project.nim

nim c -d:release -d:mingw --cpu=i386 --app:lib -o:./re.dll project_dll.nim
```

---

### Golang/Go

* Compile Golang/Go on Linux for Linux

```bash
go build hello.go
go build -o run_me hello.go
```

* Compile Golang/Goon Linux for Window

```bash
GOOS=windows GOARCH=amd64 go build -o pwn.exe runner.go
GOOS=windows GOARCH=386 go build -o pwn.exe runner.go

GOOS=windows GOARCH=amd64 go build -buildmode=c-shared -o pwn.dll loader.go
GOOS=windows GOARCH=386 go build -buildmode=c-shared -o pwn.dll loader.go
```
