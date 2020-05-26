#!/usr/bin/ruby
require 'yaml'
require 'set'

errors_found = 0

sigs = YAML.load(File.read("sig/sigs.yaml"))
known_exceptions_load = YAML.load(File.read("zh/technical-committee/governance/exceptions.yaml"))
exp_set = Array.new known_exceptions_load["exceptions"]

print "Sanity check among YAML databases inside openEuler community."

print "\n\nCheck 1: "
print "Repository in src-openeuler and openeuler usually be managed by the same SIG.\n"
repositories = Hash.new
for s in sigs do
	s[1].each { |sig| 
		next if sig["name"] == "Private"
		sig["repositories"].each { |repo|
			repo_name = repo.gsub("src-openeuler/", "").gsub("openeuler/", "")
			if repositories[repo_name] == nil then
				repositories[repo_name] = Set.new
				repositories[repo_name] << sig["name"]
			else
				repositories[repo_name] << sig["name"]
			end
		}
	}
end
repositories.each_key { |repo|
	if repositories[repo].length != 1 then
		next if exp_set.include?(repo)
		print repo, ": ", repositories[repo], "\n"
		errors_found = errors_found + 1	
	end
}
if errors_found == 0 then
	print "No issues found. PASS!"
end
errors_found = 0

print "\n\nCheck 2: "
print "Repositories in src-openeuler or openeuler should not be managed by multiple SIGs.\n"
repositories = Hash.new
for s in sigs do
	s[1].each { |sig| 
		next if sig["name"] == "Private"
		sig["repositories"].each { |repo|
			if repositories[repo] == nil then
				repositories[repo] = Set.new
				repositories[repo] << sig["name"]
			elsif repositories[repo].include?(sig["name"])
				print repo, " has been managed by ", sig["name"], " more than 1 time.\n"
				errors_found = errors_found + 1			
			else
				repositories[repo] << sig["name"]
			end
		}
	}
end
repositories.each_key { |repo|
	if repositories[repo].length != 1 then
		next if exp_set.include?(repo)
		print repo, ": ", repositories[repo], "\n"
		errors_found = errors_found + 1	
	end
}
if errors_found == 0 then
	print "No issues found. PASS!"
end
errors_found = 0

print "\n\nCheck 3: "
print "We are working on reducing Private repos, this checking is purely informative.\n"
repositories = Hash.new
for s in sigs do
	s[1].each { |sig| 
		sig["repositories"].each { |repo|
			if repositories[repo] == nil then
				repositories[repo] = Set.new
				repositories[repo] << sig["name"]
			else
				repositories[repo] << sig["name"]
			end
		}
	}
end

print "There're ", repositories.length, " repositories in total.\n" 
count = 0
private_only = 0
repositories.each_key { |repo|
	if repositories[repo].length != 1 then
		if repositories[repo].include?("Private") then
			count = count + 1
		end
	else
		if repositories[repo].include?("Private") then
			private_only = private_only + 1
		end
	end
}
print "There're ", count, " repositories co-managed by Private\n"
print "There're ", private_only, " repositories managed by Private only\n"

cross_checked_repo = Set.new

print "\n\nCheck 4: "
print "repository/openeuler.yaml should be consisitent with sigs.yaml\n"
openeuler_repo_load = YAML.load(File.read("repository/openeuler.yaml"))
openeuler_repos = openeuler_repo_load["repositories"]
openeuler_repos.each { |openeuler_repo|
	name = "openeuler/"+openeuler_repo["name"]
	if cross_checked_repo.include?(name) then
		print "Repository ", name, " in openeuler.yaml has duplication.\n"
		errors_found = errors_found + 1
	end
	if repositories[name] == nil then
		next if exp_set.include?(name)
		print "Repository ", name, " in openeuler.yaml cannot be found in sigs.yaml\n"
		errors_found = errors_found + 1		
	next
	end
	if openeuler_repo["type"] == "public" and repositories[name].include?("Private") then
		print "Repository ", name, " marked as public in openeuler.yaml, but listed in Private SIG.\n"
		errors_found = errors_found + 1	
	end
	if openeuler_repo["type"] == "private" and not repositories[name].include?("Private") then
		print "Repository ", name, " marked as private in openeuler.yaml, but not listed in Private SIG.\n"
		errors_found = errors_found + 1	
	end
	cross_checked_repo << name
}

if errors_found == 0 then
	print "No issues found. PASS!"
end
errors_found = 0

print "\n\nCheck 5: "
print "repository/src-openeuler.yaml should be consistent with sigs.yaml\n"
srcopeneuler_repo_load = YAML.load(File.read("repository/src-openeuler.yaml"))
srcopeneuler_repos = srcopeneuler_repo_load["repositories"]
srcopeneuler_repos.each { |srcopeneuler_repo|
	name = "src-openeuler/"+srcopeneuler_repo["name"]
	if cross_checked_repo.include?(name) then
		print "Repository ", name, " in src-openeuler.yaml has duplication.\n"
		errors_found = errors_found + 1
	end
	if repositories[name] == nil then
		print "Repository ", name, " in src-openeuler.yaml cannot be found in sigs.yaml\n"
		errors_found = errors_found + 1		
		next
	end
	if srcopeneuler_repo["type"] == "public" and repositories[name].include?("Private") then
		print "Repository ", name, " marked as public in src-openeuler.yaml, but listed in Private SIG.\n"
		errors_found = errors_found + 1	
	end
	if srcopeneuler_repo["type"] == "private" and not repositories[name].include?("Private") then
		print "Repository ", name, " marked as private in src-openeuler.yaml, but not listed in Private SIG.\n"
		errors_found = errors_found + 1	
	end
	cross_checked_repo << name
}

if errors_found == 0 then
	print "No issues found. PASS!"
end
errors_found = 0

print "\n\nCheck 6: "
print "All repositories in sigs.yaml must list in either openeuler.yaml or src-openeuler.yaml\n"

if cross_checked_repo.length != repositories.length then
	repositories.each_key { |n|
		next if cross_checked_repo.include?(n)
		print n, " listed in sigs.yaml, but neither openeuler.yaml nor src-openeuler.yaml\n"
		errors_found = errors_found + 1
	}
end

if errors_found == 0 then
	print "No issues found. PASS!\n"
end
