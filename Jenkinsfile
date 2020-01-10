def giteeCommentHeader = "| Check Name | Build Result | Build Details |\n| --- | --- | --- |\n"
pipeline {
    agent { node { label 'docker_enabled' } }
    environment {
        GITEE_TOKEN = credentials('new_gitee_token_id')
    }
    stages {
        stage('source code clone') {
            steps {
                checkout([$class: 'GitSCM',
                    branches: [[name: "FETCH_HEAD"]],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [[$class: 'LocalBranch'], [$class: 'RelativeTargetDirectory', relativeTargetDir: "community"]],
                    userRemoteConfigs: [[refspec: "+refs/pull/${env.giteePullRequestIid}/MERGE:refs/pull/${env.giteePullRequestIid}/MERGE",
                    url: "https://${env.GITEE_TOKEN}@gitee.com/openeuler/community"]]
                ])
            }
        }
        stage('validate user and projects'){
            parallel {
        		stage('validate gitee user') {
		            steps {
		                sh "validator owner check -f OWNERS -d  ${WORKSPACE}/community/sig -g ${GITEE_TOKEN}"
		            }
        		}
		        stage('validate gitee project') {
		            steps {
		                sh '''#!/bin/bash
                             cd ${WORKSPACE}/community
                             git fetch origin master:master
                             export OPENEULER_IGNORE=$(git diff origin/master... -- repository/openeuler.yaml | grep '^+- name:' | sed 's/+- name://g' | tr -d '[:blank:]' | awk '{printf "openeuler/%s,", $0}')
                             export SRC_OPENEULER_IGNORE=$(git diff origin/master... -- repository/src-openeuler.yaml | grep '^+- name:' | sed 's/+- name://g' | tr -d '[:blank:]' | awk '{printf "src-openeuler/%s,", $0}')
                             echo "${OPENEULER_IGNORE}${SRC_OPENEULER_IGNORE}"
                             validator sig checkrepo -f ${WORKSPACE}/community/sig/sigs.yaml -g ${GITEE_TOKEN} -i " ${OPENEULER_IGNORE}${SRC_OPENEULER_IGNORE}"
                           '''
		            }
		        }
		    }
        }

    }

    post {
        success {
        	script {
        		comments = giteeCommentHeader + "| User&Project Validation | **success** :white_check_mark: | [#${currentBuild.fullDisplayName}](${env.BUILD_URL}/console) | \n"
        	}
        	addGiteeMRComment comment: comments
            echo 'succeeeded!'
        }

        failure {
        	script {
        		comments = giteeCommentHeader + "| User&Project Validation | **failed** :x: | [#${currentBuild.fullDisplayName}](${env.BUILD_URL}/console) | \n"
        	}
        	addGiteeMRComment comment: comments
            echo 'failed :('
        }
    }
}