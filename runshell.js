const { spawn } = require('child_process');

function runScript() {
  const script = spawn('sh', ['./upload.sh']);

  script.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });

  script.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  script.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    // Restart the script
    runScript();
  });
}

// Start the script
runScript();
