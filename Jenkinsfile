pipeline {
  agent any

  environment {
    VENV = "${WORKSPACE}/venv"
    PATH = "${WORKSPACE}/venv/bin:${env.PATH}"
  }

  stages {
    stage('Build') {
      steps {
        echo '=== BUILD: Setting up Python virtual environment and installing dependencies ==='
        sh '''
          python3 -m venv venv
          . venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Test') {
      steps {
        echo '=== TEST: Running unit and integration tests with pytest ==='
        sh '''
          . venv/bin/activate
          pip install pytest
          pytest tests/ --junitxml=test-results.xml
        '''
      }
      post {
        always {
          junit 'test-results.xml'
        }
      }
    }

    stage('Code Quality') {
      steps {
        echo '=== CODE QUALITY: Running flake8 for linting ==='
        sh '''
          . venv/bin/activate
          pip install flake8
          flake8 app/
        '''
      }
    }

    stage('Security') {
      steps {
        echo '=== SECURITY: Running Bandit for security checks ==='
        sh '''
          . venv/bin/activate
          pip install bandit
          bandit -r app/
        '''
      }
    }

    stage('Deploy') {
      steps {
        echo '=== DEPLOY: Building and running with Docker Compose ==='
        sh 'docker-compose up -d --build'
      }
    }

    stage('Release') {
      steps {
        echo '=== RELEASE: Tagging this build as a release ==='
        sh '''
          git config --global user.email "ci-bot@example.com"
          git config --global user.name "CI Bot"
          git tag -a v${BUILD_NUMBER} -m "Release ${BUILD_NUMBER}"
          git push origin --tags
        '''
      }
    }

    stage('Monitoring') {
      steps {
        echo '=== MONITORING: Performing health check on running app ==='
        sh 'curl -f http://localhost:5000/ || exit 1'
      }
    }
  }
}