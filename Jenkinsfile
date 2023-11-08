pipeline {

	stages {
		/*
		 * Clone the repository on Github
		 */
		stage('Checkout SCM') {
			agent any
			steps {
				git 'https://github.com/gregerchen99/JenkinsTest.git'
			}
		}
		/*
		 * Perform OWASP Dependency Check
		 */
		stage('OWASP DependencyCheck') {
			agent any
			steps {
				dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'OWASP Dependency-Check Vulnerabilities'
			}
			post {
				success {
					dependencyCheckPublisher pattern: 'dependency-check-report.xml'
				}
			}
		}
		/*
		 *
		 */
		stage('Headless Browser Test'){
			agent {
				docker {
					image 'maven:3-alpine' 
					args '-v /root/.m2:/root/.m2' 
				}
			}
			steps {
				sh 'mvn -B -DskipTests clean package'
				sh 'mvn test'
			}
			post {
				always {
					junit 'target/surefire-reports/*.xml'
				}
			}
		}
	}	
}