#!/usr/bin/ruby
require 'yaml'
require 'set'

errors_found = 0

srcopeneuler_repo_load = YAML.load(File.read("repository/src-openeuler.yaml"))
srcopeneuler_repos = srcopeneuler_repo_load["repositories"]

sigs = YAML.load(File.read("sig/sigs.yaml"))

repositories = Hash.new
for s in sigs do
	s[1].each { |sig| 
		next if sig["name"] != "Private"
		private_set = Set.new sig["repositories"]
		srcopeneuler_repos.each { |srcopeneuler_repo|
			name = "src-openeuler/"+srcopeneuler_repo["name"]
			if srcopeneuler_repo["type"] == "public" and private_set.include?(name) then
				private_set.delete name
			end
		}
		sig["repositories"] = private_set.to_a
		print sig["repositories"]
	}
end

File.open("new-sigs.yaml", "w") { |file| file.write(sigs.to_yaml) }
