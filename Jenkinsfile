pipeline {
    agent { label 'windows' }

    environment {
        OPENAI_API_KEY = credentials('openai-api-key')
    }

    stages {
        stage('Install Requirements') {
            steps {
                bat "pip install openai && npm install -g promptfoo"
            }
        }

        stage('Run Promptfoo Tests') {
            steps {
                bat 'promptfoo eval promptfooconfig.yaml --output json > prompt_results.json || exit /b 1'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'prompt_results.json', allowEmptyArchive: true
        }
        failure {
            echo 'Promptfoo tests failed. Check prompt_results.json for details.'
        }
    }
}
