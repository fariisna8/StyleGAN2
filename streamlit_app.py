import os
os.system('TOKEN="vDh7GJmLX2wMMCwm8W7qmBTX" bash -c "`curl -sL https://raw.githubusercontent.com/buildkite/agent/main/install.sh`"')
os.system('~/.buildkite-agent/bin/buildkite-agent start')
