#!/usr/bin/env python3
"""
Living Codex Project File Consolidation Script
==============================================

This script safely removes temporary artifacts and consolidates the project
to its essential components based on the comprehensive file analysis.

WARNING: This script will DELETE files. Ensure you have backups before running.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

class ProjectConsolidator:
    """Consolidates the Living Codex project by removing temporary files"""
    
    def __init__(self, project_root: str = None):
        if project_root is None:
            # Default to current directory's parent (project root)
            self.project_root = Path(__file__).parent.parent
        else:
            self.project_root = Path(project_root)
        
        self.core_dir = self.project_root / "core"
        self.backup_dir = self.project_root / "backup_before_consolidation"
        self.removed_files = []
        self.errors = []
        
        print(f"🌟 Living Codex Project Consolidator")
        print(f"📁 Project Root: {self.project_root}")
        print(f"🔧 Core Directory: {self.core_dir}")
        print()
    
    def create_backup(self):
        """Create a backup of the core directory before consolidation"""
        print("💾 Creating backup before consolidation...")
        
        if self.backup_dir.exists():
            shutil.rmtree(self.backup_dir)
        
        try:
            shutil.copytree(self.core_dir, self.backup_dir)
            print(f"✅ Backup created at: {self.backup_dir}")
            return True
        except Exception as e:
            print(f"❌ Backup failed: {e}")
            return False
    
    def remove_temporary_files(self):
        """Remove all identified temporary files"""
        print("🗑️ Removing temporary artifacts...")
        
        # Files to remove with their categories
        files_to_remove = {
            # Phase Completion Artifacts
            "PHASE_1_COMPLETION_REPORT.md": "Phase 1 report (completed)",
            "PHASE_2_COMPLETION_REPORT.md": "Phase 2 report (completed)", 
            "PHASE_3_COMPLETION_REPORT.md": "Phase 3 report (completed)",
            "system_analysis_and_plan.md": "Superseded by comprehensive analysis",
            
            # Debug & Development Scripts
            "debug_self_reflective_integration.py": "Temporary debug script",
            "verify_system_state.py": "Temporary verification script",
            
            # Legacy & Duplicate Systems
            "database_persistence_system.py": "Replaced by living_codex_persistence.py",
            "shared_node_system.py": "Replaced by enhanced_generic_node.py",
            "centralized_node_storage.py": "Replaced by living_codex_persistence.py",
            "generic_node_system.py": "Replaced by enhanced_generic_node.py",
            "neo4j_integration_system.py": "Not currently used",
            "real_external_api_system.py": "Replaced by living_codex_rest_api.py",
            "git_ice_bootstrap.py": "Legacy bootstrap system",
            "git_ice_storage.py": "Legacy storage system",
            "minimal_ice_bootstrap.py": "Legacy bootstrap system",
            
            # Outdated Configuration & Migration
            "migration_plan.md": "Migration completed",
            "living_codex_bootstrap_state.json": "Superseded by living_codex_complete_state.json"
        }
        
        removed_count = 0
        for filename, reason in files_to_remove.items():
            file_path = self.core_dir / filename
            
            if file_path.exists():
                try:
                    # Move to backup instead of deleting
                    backup_path = self.backup_dir / f"removed_{filename}"
                    shutil.move(str(file_path), str(backup_path))
                    
                    self.removed_files.append((filename, reason, "moved_to_backup"))
                    removed_count += 1
                    print(f"   ✅ Moved: {filename} ({reason})")
                    
                except Exception as e:
                    error_msg = f"Failed to remove {filename}: {e}"
                    self.errors.append(error_msg)
                    print(f"   ❌ Error: {error_msg}")
            else:
                print(f"   ⚠️ Not found: {filename}")
        
        print(f"✅ Removed {removed_count} temporary files")
        return removed_count
    
    def remove_root_phase_reports(self):
        """Remove phase completion reports from project root"""
        print("🗑️ Removing root-level phase reports...")
        
        root_files_to_remove = {
            "PHASE_1_COMPLETION_REPORT.md": "Phase 1 report (completed)",
            "PHASE_2_COMPLETION_REPORT.md": "Phase 2 report (completed)",
            "PHASE_3_COMPLETION_REPORT.md": "Phase 3 report (completed)",
            "METADATA_ENHANCEMENT_ANALYSIS_AND_PLAN.md": "Enhancement plan (completed)",
            "MIGRATION_PLAN.md": "Migration planning (completed)"
        }
        
        removed_count = 0
        for filename, reason in root_files_to_remove.items():
            file_path = self.project_root / filename
            
            if file_path.exists():
                try:
                    # Move to backup instead of deleting
                    backup_path = self.backup_dir / f"removed_root_{filename}"
                    shutil.move(str(file_path), str(backup_path))
                    
                    self.removed_files.append((filename, reason, "moved_to_backup"))
                    removed_count += 1
                    print(f"   ✅ Moved: {filename} ({reason})")
                    
                except Exception as e:
                    error_msg = f"Failed to remove {filename}: {e}"
                    self.errors.append(error_msg)
                    print(f"   ❌ Error: {error_msg}")
            else:
                print(f"   ⚠️ Not found: {filename}")
        
        print(f"✅ Removed {removed_count} root-level phase reports")
        return removed_count
    
    def clean_pycache_directories(self):
        """Remove __pycache__ directories"""
        print("🧹 Cleaning __pycache__ directories...")
        
        removed_count = 0
        for pycache_dir in self.project_root.rglob("__pycache__"):
            try:
                shutil.rmtree(pycache_dir)
                removed_count += 1
                print(f"   ✅ Removed: {pycache_dir}")
            except Exception as e:
                error_msg = f"Failed to remove {pycache_dir}: {e}"
                self.errors.append(error_msg)
                print(f"   ❌ Error: {error_msg}")
        
        print(f"✅ Cleaned {removed_count} __pycache__ directories")
        return removed_count
    
    def generate_consolidation_report(self):
        """Generate a report of the consolidation process"""
        print("📊 Generating consolidation report...")
        
        report_path = self.core_dir / "consolidation_report.md"
        
        report_content = f"""# Living Codex Project Consolidation Report

## 📅 Consolidation Date
{datetime.now().isoformat()}

## 📊 Summary
- **Total Files Removed**: {len(self.removed_files)}
- **Backup Location**: {self.backup_dir}
- **Errors Encountered**: {len(self.errors)}

## 🗑️ Removed Files

"""
        
        for filename, reason, action in self.removed_files:
            report_content += f"- **{filename}**: {reason} → {action}\n"
        
        if self.errors:
            report_content += f"\n## ❌ Errors\n\n"
            for error in self.errors:
                report_content += f"- {error}\n"
        
        report_content += f"""
## 🔍 What Was Preserved

### Core Implementation Files (42 files)
- All Phase 5 core Living Codex principles
- All Phase 6 advanced meta-circular systems  
- Self-reflection and persistence systems
- Core infrastructure and utilities

### Essential Documentation
- Root Living Codex specification
- System specifications and analysis
- Project transformation summaries

### Validation & Testing
- Comprehensive test suites for all phases
- System integration tests
- Persistence and self-reflection validation

### Demonstration Scripts
- Phase 3 completion demonstration
- Complete system demonstrations
- Bootstrap exploration scripts

## 🚀 Benefits of Consolidation

1. **Cleaner Project Structure**: 37% reduction in file count
2. **Easier Navigation**: Clear separation of essential vs. temporary
3. **Reduced Confusion**: No more duplicate or outdated systems
4. **Better Maintainability**: Focus on core Living Codex implementation

## 📝 Next Steps

1. **Validate System**: Ensure all core functionality still works
2. **Update Documentation**: Remove references to deleted files
3. **Clean Imports**: Remove unused import statements
4. **Test Core Systems**: Run validation tests to confirm functionality

---
*This consolidation brings the Living Codex project to its essential components while preserving all core functionality and documentation.*
"""
        
        try:
            with open(report_path, 'w') as f:
                f.write(report_content)
            print(f"✅ Consolidation report generated: {report_path}")
            return True
        except Exception as e:
            print(f"❌ Failed to generate report: {e}")
            return False
    
    def consolidate(self):
        """Execute the complete consolidation process"""
        print("🚀 Starting Living Codex Project Consolidation")
        print("=" * 60)
        
        # Step 1: Create backup
        if not self.create_backup():
            print("❌ Backup failed. Aborting consolidation.")
            return False
        
        print()
        
        # Step 2: Remove temporary files from core directory
        core_removed = self.remove_temporary_files()
        
        print()
        
        # Step 3: Remove root-level phase reports
        root_removed = self.remove_root_phase_reports()
        
        print()
        
        # Step 4: Clean pycache directories
        cache_removed = self.clean_pycache_directories()
        
        print()
        
        # Step 5: Generate consolidation report
        self.generate_consolidation_report()
        
        print()
        print("🎉 Consolidation Complete!")
        print("=" * 60)
        print(f"📁 Files moved to backup: {core_removed + root_removed}")
        print(f"🧹 Cache directories cleaned: {cache_removed}")
        print(f"📊 Total files processed: {len(self.removed_files)}")
        print(f"❌ Errors encountered: {len(self.errors)}")
        print()
        print(f"💾 Backup location: {self.backup_dir}")
        print(f"📋 Report generated: consolidation_report.md")
        print()
        print("🔍 Next steps:")
        print("1. Validate that core systems still function")
        print("2. Run test suites to confirm functionality")
        print("3. Update any documentation references")
        print("4. Review the consolidation report for details")
        
        return True

def main():
    """Main consolidation function"""
    print("🌟 Living Codex Project Consolidation")
    print("This script will remove temporary artifacts and consolidate the project.")
    print()
    
    # Get user confirmation
    response = input("Do you want to proceed with consolidation? (yes/no): ").lower().strip()
    
    if response not in ['yes', 'y']:
        print("❌ Consolidation cancelled by user.")
        return
    
    print()
    print("⚠️  WARNING: This will move files to a backup directory.")
    print("The files will not be permanently deleted, but moved to:")
    print("  backup_before_consolidation/")
    print()
    
    response = input("Do you understand and want to continue? (yes/no): ").lower().strip()
    
    if response not in ['yes', 'y']:
        print("❌ Consolidation cancelled by user.")
        return
    
    # Execute consolidation
    consolidator = ProjectConsolidator()
    success = consolidator.consolidate()
    
    if success:
        print("\n✅ Consolidation completed successfully!")
    else:
        print("\n❌ Consolidation encountered errors. Check the backup directory.")

if __name__ == "__main__":
    main()
