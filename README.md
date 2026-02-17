[![progress-banner](https://backend.codecrafters.io/progress/shell/314bb025-8cb0-49a4-a609-ec5bb4bfc3bd)](https://app.codecrafters.io/users/codecrafters-bot?r=2qF)

This is a starting point for Python solutions to the
["Build Your Own Shell" Challenge](https://app.codecrafters.io/courses/shell/overview).

In this challenge, you'll build your own POSIX compliant shell that's capable of
interpreting shell commands, running external programs and builtin commands like
cd, pwd, echo and more. Along the way, you'll learn about shell command parsing,
REPLs, builtin commands, and more.

**Note**: If you're viewing this repo on GitHub, head over to
[codecrafters.io](https://codecrafters.io) to try the challenge.

# Passing the first stage

The entry point for your `shell` implementation is in `app/main.py`. Study and
uncomment the relevant code, and push your changes to pass the first stage:

```sh
git commit -am "pass 1st stage" # any msg
git push origin master
```

Time to move on to the next stage!

# Stage 2 & beyond

Note: This section is for stages 2 and beyond.

1. Ensure you have `uv` installed locally
1. Run `./your_program.sh` to run your program, which is implemented in
   `app/main.py`.
1. Commit your changes and run `git push origin master` to submit your solution
   to CodeCrafters. Test output will be streamed to your terminal.

## python knowledge
## Locate executable files
- 쉘에서 ‎`PATH="..." ./your_program.sh` 로 실행하면, 그 PATH는 자식 프로세스(Python 프로그램)의 환경변수로 전달
- Python에서는 ‎`os.environ["PATH"]` 또는 ‎`os.getenv("PATH")` 로 
- 디렉터리 목록으로 나누려면 ‎`path_value.split(os.pathsep)` 를 사용
- `None`을 체크할 때는 항상 ‎`is` / ‎`is not` 을 사용
