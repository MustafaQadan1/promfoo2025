pipeline {
  agent any

//   environment {
//     OPENAI_API_KEY = credentials('openai-api-key')
//   }

  stages {
    stage('Checkout') {
        steps {
            checkout([
            $class: 'GitSCM',
            branches: [[name: 'refs/heads/main']],
            doGenerateSubmoduleConfigurations: false,
            extensions: [],
            userRemoteConfigs: [[url: 'https://github.com/MustafaQadan1/promfoo2025.git']]
            ])
        }
        }

    stage('Set Up Virtual Environment') {
      steps {
        bat 'python -m venv venv'
      }
    }

    stage('Install Dependencies') {
      steps {
        bat '.\\venv\\Scripts\\activate && pip install -r requirements.txt'
      }
    }

        stage('Run Flask App in Background') {
        steps {
            bat """
            .\\venv\\Scripts\\activate
            start /B python chatbot_api.py
            """
            sleep time: 10, unit: 'SECONDS'
        }
        }

        stage('Run Promptfoo Tests') {
        steps {
            bat """
            .\\venv\\Scripts\\activate
            promptfoo eval --config promptfooconfig.yaml
            """
        }
        }
  }

  post {
    always {
      echo 'Pipeline finished.'
    }
  }
}