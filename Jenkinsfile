pipeline {
    agent any

    stages {
        stage('Headless Browser Test') {
            steps {
                script {
                    // Pull the Maven Docker image
                    sh 'docker pull maven:3-alpine'

                    // Run Maven commands within the Maven Docker container
                    sh 'docker run -v /root/.m2:/root/.m2 -v $PWD:/usr/src/myapp -w /usr/src/myapp maven:3-alpine mvn -B -DskipTests clean package'
                    sh 'docker run -v /root/.m2:/root/.m2 -v $PWD:/usr/src/myapp -w /usr/src/myapp maven:3-alpine mvn test'
                }
            }
            post {
                always {
                    junit 'target/surefire-reports/*.xml'
                }
            }
        }
    }
}
