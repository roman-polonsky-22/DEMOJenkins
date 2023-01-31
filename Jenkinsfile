pipeline {
  agent any
  stages {
    stage("verify tooling") {
      steps {
        sh '''
          docker version
          docker info
          docker compose version 
          curl --version
        '''
      }
    }
    stage('Prune Docker data') {
      steps {
        sh 'docker system prune -a --volumes -f'
      }
    }
    stage('Start container') {
      steps {
        sh 'docker compose up -d --wait'
        sh 'docker compose ps'
      }
    }
    stage('Run tests against the nginx') {
      steps {
        sh 'curl http://localhost'
      }
    }
    stage('Push image') {
      steps {
        withDockerRegistry([ credentialsId: "rompolodockerhub", url: "" ]) {
        dockerImage.push()
        }
      }
    } 
  }
  post {
    always {
      sh 'docker compose down --remove-orphans -v'
      sh 'docker compose ps'
    }
  }
}
